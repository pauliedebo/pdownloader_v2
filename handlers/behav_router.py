import asyncio
from aiogram import types, F, Router

video_link = ""
f = 0
link_router = Router()

@link_router.message(F.text == "Download")
async def link(message: types.Message):
    global f
    await message.answer("Send me a link to the video: ")
    f = 1

@link_router.message(lambda message: ("youtube.com" in message.text or "youtu.be" in message.text) and f == 1)
async def video(message: types.Message):
    global video_link
    await message.answer("Got your link! Proceeding...")
    video_link = message.text
