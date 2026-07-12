import subprocess

FORMATS = [144, 240, 360, 480, 720, 1080]

def quality_checker(link):
    t = subprocess.run(["yt-dlp", "-F", link], capture_output=True, text=True)
    table = t.stdout.strip()
    if not "ERROR" in table:
        table = table.split('\n')
        table = [i for i in table if not i.startswith('[')]
        available_formats = set()
        for i in table:
            for j in range(len(FORMATS)):
                if str(FORMATS[j])+'p' in i:
                    available_formats.add(FORMATS[j])
        available_formats = sorted(list(available_formats))
        return available_formats
                

def downloader(link, quality):
    n = subprocess.run(["yt-dlp", "--print", "title", "--no-warnings", link], capture_output=True, text=True)
    name = n.stdout.strip()
    if not "ERROR" in name:
        ch = subprocess.run(["yt-dlp", "--print", "channel", "--no-warnings", link], capture_output=True, text=True)
        channel = ch.stdout.strip()
        download = subprocess.run(["yt-dlp", "--embed-thumbnail", "-S", f"res:{quality}", "-o", f"Downloaded/{name}-{quality}p.%(ext)s", link], capture_output=True, text=True)
        download_status = download.stdout.strip()
        f = subprocess.run(["find", "Downloaded", "-name", f"{name}*{quality}p*"], capture_output=True, text=True)
        filename = f.stdout.strip().split('/')[-1]
        subprocess.run(["ffmpeg", "-n", "-i", f"Downloaded/{filename}", f"Downloaded/{name}-{quality}p.mp4"])
        subprocess.run(["rm", f"Downloaded/{filename}"])
        
        final_file = f"{name}-{quality}p.mp4"

        return channel, name, final_file

def audio_downloader(link):
    n = subprocess.run(["yt-dlp", "--print", "title", "--no-warnings", link], capture_output=True, text=True)
    name = n.stdout.strip()
    if not "ERROR" in name:
        ch = subprocess.run(["yt-dlp", "--print", "channel", "--no-warnings", link], capture_output=True, text=True)
        channel = ch.stdout.strip()
        subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', f"Downloaded/{name}.%(ext)s", link], capture_output=True, text=True)
        filename = f"{name}.mp3"

        return channel, name, filename

def thumb_downloader(link):
    n = subprocess.run(["yt-dlp", "--print", "title", "--no-warnings", link], capture_output=True, text=True)
    name = n.stdout.strip()
    if not "ERROR" in name:
        ch = subprocess.run(["yt-dlp", "--print", "channel", "--no-warnings", link], capture_output=True, text=True)
        channel = ch.stdout.strip()
        thumb = subprocess.run(["yt-dlp", "--write-thumbnail", "--skip-download", "--convert-thumbnails", "jpg", "-o", f"Downloaded/{name}.%(ext)s", link])
        thumbnail = f"{name}.jpg"

        return name, channel, thumbnail

def deletion(path):
    subprocess.run(["rm", f"Downloaded/{path}"])
