from string import punctuation
from aiogram import types, Router


user_group_router = Router()

rsda = {'вы','lala'}

def clean_text(text: str):
    return text.translate(str.maketrans('','',punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if rsda.intersection(clean_text(message.text.lower())):
        await message.answer(f"{message.from_user.first_name}, соблюдайте порядок в чате")
        await message.delete()
        # await message.chat.ban(message.from_user.id) для блокировки пользователей