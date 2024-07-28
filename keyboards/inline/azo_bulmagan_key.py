from models.models import Channel

from aiogram.utils.keyboard import InlineKeyboardBuilder

def keyboard(azo_bulmagan):
    k = InlineKeyboardBuilder()
    
    for kanal in azo_bulmagan:
        kanal : Channel
        k.button(text=kanal.name, url=kanal.link)
    k.button(text="Tekshirish ✅", callback_data='tekshirish')
    k.adjust(1)
    
    return k.as_markup()