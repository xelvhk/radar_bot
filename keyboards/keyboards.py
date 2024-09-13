from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton
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


ans_button_1 = KeyboardButton(text=LEXICON_RU['answers']['place'])
ans_button_2 = KeyboardButton(text=LEXICON_RU['answers']['uvs'])
ans_button_3 = KeyboardButton(text=LEXICON_RU['answers']['uvc'])
ans_button_4 = KeyboardButton(text=LEXICON_RU['answers']['mk'])
ans_button_5 = KeyboardButton(text=LEXICON_RU['answers']['sick'])
ans_button_6 = KeyboardButton(text=LEXICON_RU['answers']['vacation'])
ans_button_7 = KeyboardButton(text=LEXICON_RU['oi'])
ans_button_8 = KeyboardButton(text=LEXICON_RU['back'])

# Создаем клавиатуру функций
ans_kb = ReplyKeyboardMarkup(
    keyboard=[[ans_button_1],
              [ans_button_2],
              [ans_button_3],
              [ans_button_4],
              [ans_button_5],
              [ans_button_6],
              [ans_button_7],
              [ans_button_8]],
    resize_keyboard=True
)
