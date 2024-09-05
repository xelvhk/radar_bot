from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU


# Создаем кнопки клавиатуры
volk_button_1 = KeyboardButton(text=LEXICON_RU['joke'])
volk_button_2 = KeyboardButton(text=LEXICON_RU['mark'])

# Создаем клавиатуру функций
volk_kb = ReplyKeyboardMarkup(
    keyboard=[[volk_button_1],
              [volk_button_2]],
    resize_keyboard=True
)
