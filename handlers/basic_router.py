from aiogram import Router, types
from aiogram.filters.command import Command

command_router = Router()

@command_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hi there! I\'m a bot that will download anything in highest quality, without asking to to subscribe to anything!\nReady to destroy YouTube?🚀")

