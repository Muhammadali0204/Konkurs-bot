from datetime import date
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.config import OYLAR


def keyboard(hafta):
    k = InlineKeyboardBuilder()
    for kun in hafta:
        kun : date
        k.button(text=f'{kun.day}-{OYLAR[kun.month]}', callback_data=str(kun))
    k.button(text="◀️Ortga", callback_data='ortga')
    k.adjust(2)
    return k.as_markup()
