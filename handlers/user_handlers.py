from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import volk_kb, ans_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_joke

router = Router()
bot = Bot

user_data = {}

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=volk_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# Вывод шуток и контроль присутствия
@router.message(F.text.in_([LEXICON_RU['joke']]))
async def send_joke(message: Message):
    joke = get_joke()
    await message.answer(joke)

@router.message(F.text.in_([LEXICON_RU['mark']]))
async def weather_command(message: Message):
    await message.reply(text=LEXICON_RU['choice'],
                        reply_markup=ans_kb)

# @router.message(F.data)
# async def handle_status(message: Message):
#     user_id = message.from_user.id
#     username = message.from_user.username
#     status = message.text
#     user_data[user_id] = {"username": username, "status": status}
#     await message.reply(f"Ваш статус:{status} записан",reply_markup=reply_keyboard_remove())
