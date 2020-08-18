from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='BTC'), KeyboardButton(text='ETH')
        ],
        [
         KeyboardButton(text='APL'), KeyboardButton(text='PAT')
        ]
    ],
    resize_keyboard=True
)