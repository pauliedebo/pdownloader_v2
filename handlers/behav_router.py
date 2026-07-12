import asyncio
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from states import YTLink

from processes import quality, video_download, audio_download, thumb_download, deletion

f = 0
link_router = Router()

@link_router.message(F.text == "Download")
async def link(message: types.Message, state: FSMContext):
    global f
    await message.answer("Send me a link to the video: ")
    await state.set_state(YTLink.waiting)
    f = 1

@link_router.message(YTLink.waiting, lambda message: ("youtube.com" in message.text or "youtu.be" in message.text) and f == 1)
async def video(message: types.Message, state: FSMContext):
    await state.update_data(user_link=message.text)
    await message.answer("Got your link! Proceeding...")
    
    data = await state.get_data()
    link = data.get("user_link")
    await message.answer(f"Your link: {link}")

    await state.clear()


