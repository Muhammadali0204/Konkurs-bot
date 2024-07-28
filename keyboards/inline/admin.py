from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foydalanuvchilar soni", callback_data="soni")
        ],
        [
            InlineKeyboardButton(text="Reklama", callback_data='reklama')
        ]
    ]
)
