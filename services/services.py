from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
import requests


def get_joke() -> str:
    joke_url = f"http://rzhunemogu.ru/RandJSON.aspx?CType=1"
    joke_response = requests.get(joke_url)
    joke_data = joke_response.json(strict=False)
    if joke_response.status_code == 200:
        joke_result = joke_data['content']
    else:
        joke_result = "Не получается пошутить"
    return joke_result
