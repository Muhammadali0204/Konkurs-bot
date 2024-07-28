from loader import bot
from models.models import session, Channel


async def azolikka_tek(user_id):
    kanallar = session.query(Channel).all()
    
    azo_bulmagan = []
    for kanal in kanallar:
        t = await bot.get_chat_member(kanal.channel_id, user_id)
        if t.status == "left":
            azo_bulmagan.append(kanal)

    return azo_bulmagan
