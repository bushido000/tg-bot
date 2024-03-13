from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start(message : types.Message):
    await message.answer('окей, начинаем викторину')

@user_private_router.message(or_f(Command('info'),(F.text == 'инфо')))
async def info_cmd(message : types.Message):
    await message.answer('вот информация о нашем боте викторины')

@user_private_router.message(F.text == 'helloy')
async def helloy(message : types.Message):
    await message.answer('Ёу, вы написали боту викторины')



