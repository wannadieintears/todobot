import asyncpg
from keyboards import keyboards
from aiogram import F, Router
from aiogram.types import Message
from utils.states import Add_next_message, Delete_next_message
from aiogram.fsm.context import FSMContext
import settings

router = Router()

@router.message(F.text.lower() == "/start")
async def start(message: Message):
    await message.answer("I'm a bot for saving your todos. Good luck, have fun! :)", reply_markup=keyboards.kb)


@router.message(F.text.lower() == "add a todo")
async def get_add_todo(message: Message, state: FSMContext):
    await state.set_state(Add_next_message.mes)
    await message.answer("Tell me what do you wanna add in your todo.")


@router.message(Add_next_message.mes)
async def add_todo(message: Message, state: FSMContext):
    await state.update_data(mes=message.text)
    await state.clear()

    connect = await asyncpg.connect(
        host=settings.host,
        port=settings.port,
        user=settings.user,
        password=settings.password,
        database=settings.database
    )

    query = f"INSERT INTO todos (todo, user_id) VALUES ('{message.text}', {message.from_user.id});"
    async with connect.transaction():
        await connect.execute(query)
        await message.answer(f"{message.text} is successful added!", reply_markup=keyboards.kb)
    await connect.close()


@router.message(F.text.lower() == "delete a todo")
async def get_delete_todo(message: Message, state: FSMContext):
    await state.set_state(Delete_next_message.mes)
    await message.answer("Tell me what do you wanna delete in your todo."
                         "Please, be sure in writing the todo in the exact way, how it's written in database!")


@router.message(Delete_next_message.mes)
async def delete_todo(message: Message, state: FSMContext):
    await state.update_data(mes=message.text)
    await state.clear()

    connect = await asyncpg.connect(
        host=settings.host,
        port=settings.port,
        user=settings.user,
        password=settings.password,
        database=settings.database
    )

    query = f"DELETE FROM todos WHERE user_id = {message.from_user.id} AND todo = '{message.text}';"
    async with connect.transaction():
        await connect.execute(query)
        await message.answer(f"{message.text} is successful added!", reply_markup=keyboards.kb)
    await connect.close()


@router.message(F.text.lower() == "show todos")
async def show_todos(message: Message):
    connect = await asyncpg.connect(
        host=settings.host,
        port=settings.port,
        user=settings.user,
        password=settings.password,
        database=settings.database
    )

    query = f"SELECT * FROM todos WHERE user_id = {message.from_user.id};"
    async with connect.transaction():
        todos = await connect.fetch(query)
        todos = '\n'.join([todo['todo'] for todo in todos])
        await message.answer(f"Your todos:\n{todos}")
    await connect.close()


@router.message()
async def what(message: Message):
    await message.answer("I didn't understand you :(", reply_markup=keyboards.kb)