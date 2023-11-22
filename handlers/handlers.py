import aiohttp
import asyncpg
from keyboards import keyboards
from aiogram import F, Router
from aiogram.types import Message
from utils.states import Next_message
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text.lower() == "/start")
async def start(message: Message):
    await message.answer("I'm a bot for saving your todos. Good luck, have fun! :)", reply_markup=keyboards.kb)


