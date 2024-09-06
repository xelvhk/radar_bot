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


ans_button_1 = KeyboardButton(text=LEXICON_RU['place'])
ans_button_2 = KeyboardButton(text=LEXICON_RU['uvs'])
ans_button_3 = KeyboardButton(text=LEXICON_RU['uvc'])
ans_button_4 = KeyboardButton(text=LEXICON_RU['mk'])
ans_button_5 = KeyboardButton(text=LEXICON_RU['sick'])
ans_button_6 = KeyboardButton(text=LEXICON_RU['vacation'])

# Создаем клавиатуру функций
ans_kb = ReplyKeyboardMarkup(
    keyboard=[[ans_button_1],
              [ans_button_2],
              [ans_button_3],
              [ans_button_4],
              [ans_button_5],
              [ans_button_6]],
    resize_keyboard=True
)

# builder = InlineKeyboardBuilder()
# builder.button(text="Я на работе!", callback_data="checkin")
# builder.button(text="УВС", callback_data="uvs")
# builder.button(text="УВЦ", callback_data="uvc")
# builder.button(text="МК", callback_data="mk")
# builder.button(text="Болею", callback_data="sick")
# builder.button(text="Отпуск", callback_data="vacation")