from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎁Giveawaylar ro'yxatini olish")
        ],
        [
            KeyboardButton(text="🕙Keyingi tugmalar tez orada qo'shiladi...")
        ]
    ],
    resize_keyboard=True
)
