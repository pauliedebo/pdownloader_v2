import asyncio
import logging

import os
from dotenv import load_dotenv

import subprocess

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from states import YTLink
from handlers.behav_router import link_router

from handlers.basic_router import command_router


logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN=os.getenv("P_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())




async def main():
    dp.include_router(command_router)
    dp.include_router(link_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
