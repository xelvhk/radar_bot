from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import volk_kb, ans_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_joke

router = Router()
bot = Bot

user_status = {}

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

@router.message(F.text.in_([LEXICON_RU['back']]))
async def weather_command(message: Message):
    await message.reply(text=LEXICON_RU['done'],
                        reply_markup=volk_kb)

def count_status(num):
    count = 0
    if num:
        count += 1
    return count

@router.message(F.text.in_(LEXICON_RU['answers']['place']+LEXICON_RU['answers']['uvs']+LEXICON_RU['answers']['uvc']+LEXICON_RU['answers']['mk']+LEXICON_RU['answers']['sick']+LEXICON_RU['answers']['vacation']+LEXICON_RU['oi']))
async def handle_status(message: Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    status = message.text

    if status == LEXICON_RU['oi']:
        if user_id in user_status:
            del user_status[user_id]
            result=f"{username}, всё - память стёрта"
        else:
            result=f"{username}, стирать пока нечего"
    else:
        if user_id not in user_status:
            user_status[user_id] = {"username": username, "status": status}
            result = f"Спасибо, {username}, Ваш статус - {status} записан"
        else:
            result = f"{username}, ты уже тыкал"
    await message.reply(result)
