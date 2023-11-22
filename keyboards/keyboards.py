from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Add a todo"),
            KeyboardButton(text="Delete a todo"),
            KeyboardButton(text="Show todos")
        ]
    ],
    resize_keyboard=True,
    selective=True
)