import asyncio, datetime

from typing import List
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from telethon.tl.types import MessageMediaGiveaway
from telethon.tl.types import Message as Telethon_msg
from aiogram import Router, filters, F, enums

from loader import bot, client
from utils import azolikka_tek
from keyboards.reply import menu
from states.user_state import States
from models.models import session, User
from keyboards.inline import azo_bulmagan_key, hafta_key
from data.config import (
    OYLAR, CHANNEL_USERNAME, PREMIUM_PHOTO
)



router = Router()
router.message.filter(F.chat.type == enums.chat_type.ChatType.PRIVATE)
router.callback_query.filter(F.message.chat.type == enums.chat_type.ChatType.PRIVATE)

# @router.message()
# async def knlvf(msg : types.Message):
#     print(msg.photo[-1].file_id)

# @router.message()
# async def knlvf(msg : types.Message):
#     print(msg.video.file_id)

@router.message(filters.CommandStart(), filters.StateFilter(None))
async def start(msg : Message, command : filters.CommandObject, state : FSMContext):
    user = session.query(User).filter_by(id = msg.from_user.id).first()
    if user is None:
        new_user = User(id = msg.from_user.id, name = msg.from_user.first_name, username = msg.from_user.username)
        session.add(new_user)
        session.commit()
    else:
        if user.name != msg.from_user.first_name or user.username != msg.from_user.username:
            user.name = msg.from_user.first_name
            user.username = msg.from_user.username
            session.commit()
        
    text = f"<b>Assalomu alaykum, {msg.from_user.mention_html(msg.from_user.first_name)}\n\nUshbu botdan bir qancha foydali ma'lumotlarni olishingiz mumkin 😊</b>"
    
    azo_bulmagan = await azolikka_tek.azolikka_tek(msg.from_user.id)
    if azo_bulmagan == []:
        await msg.answer(text=text, reply_markup=menu.menu)
    else:
        await msg.answer(text=text)
        await msg.answer("<b>Botdan foydalana olish uchun quyidagi kanallarga obuna bo'ling !</b>", reply_markup=azo_bulmagan_key.keyboard(azo_bulmagan))
        await state.set_state(States.kanalga_azo)
        
@router.callback_query(F.data == "tekshirish", States.kanalga_azo)
async def check(call : CallbackQuery, state : FSMContext):
    azo_bulmagan = await azolikka_tek.azolikka_tek(call.from_user.id)
    if azo_bulmagan != []:
        await call.answer("Siz barcha kanallarga a'zo bo'lmadingiz ❗️", show_alert=True)
        try :
            await call.message.edit_text("<b>Siz barcha kanallarga a'zo bo'lmadingiz ❗️</b>", reply_markup=azo_bulmagan_key.keyboard(azo_bulmagan))
        except :
            pass
    else:
        await call.message.delete()
        await state.clear()
        await call.message.answer("<b>Tabriklaymiz 🎉 Botdan foydalanishingiz mumkin !</b>", reply_markup=menu.menu)
        
@router.message(States.kanalga_azo)
async def check2(msg : Message, state : FSMContext):
    azo_bulmagan = await azolikka_tek.azolikka_tek(msg.from_user.id)
    if azo_bulmagan != []:
        await msg.answer("<b>Botdan foydalana olish uchun quyidagi kanallarga obuna bo'ling !</b>", reply_markup=azo_bulmagan_key.keyboard(azo_bulmagan))
    else:
        await state.clear()
        await msg.answer("<b>Tabriklaymiz 🎉 Botdan foydalanishingiz mumkin !</b>", reply_markup=menu.menu)

@router.message(F.text == "🎁Giveawaylar ro'yxatini olish")
async def get_giveaway(msg : Message, state : FSMContext):
    today = datetime.date.today()
    hafta = [today + datetime.timedelta(days=i) for i in range(0, 7)]
    text = f"<b>Qaysi kungi giveawaylar ro'yxati kerak ❓</b>"
    await msg.answer(text=text, reply_markup=hafta_key.keyboard(hafta))
    await state.set_state(States.ruyxat)

@router.callback_query(States.ruyxat)
async def ruyxat(call : CallbackQuery, state : FSMContext):
    await call.message.delete()
    data = call.data
    
    if data == 'ortga':
        await call.message.answer("<b>Menu :</b>", reply_markup=menu.menu)
    else:
        date = datetime.date.fromisoformat(data)
        today_giveaways : List[Telethon_msg] = []
    
        async for give in client.iter_messages('giveaways_tg_uz'):
            if type(give) == Telethon_msg and type(give.media) == MessageMediaGiveaway:
                give_date = give.media.until_date + datetime.timedelta(hours=5)
                if give_date.date() == date:
                    today_giveaways.append(give)
                         
        for i in range(0, len(today_giveaways)):
            for j in range(0,len(today_giveaways) - i - 1):
                if today_giveaways[j].media.until_date == today_giveaways[j+1].media.until_date:
                    if today_giveaways[j].media.quantity == today_giveaways[j+1].media.quantity:
                        if today_giveaways[j].media.months > today_giveaways[j].media.months:
                            today_giveaways[j].media.quantity == today_giveaways[j+1].media.quantity
                    elif today_giveaways[j].media.quantity > today_giveaways[j+1].media.quantity:
                        today_giveaways[j], today_giveaways[j+1] = today_giveaways[j+1], today_giveaways[j]
                elif today_giveaways[j].media.until_date > today_giveaways[j+1].media.until_date:
                    today_giveaways[j], today_giveaways[j+1] = today_giveaways[j+1], today_giveaways[j]
        text2 = ""
        i = 1
        for msg in today_giveaways:
            msg : Telethon_msg
            text2 += f"{i}. <a href = 'https://t.me/giveaways_tg_uz/{msg.id}'>{msg.media.quantity} ta {msg.media.months} oy {(msg.media.until_date + datetime.timedelta(hours=5)).time()}</a>\n"
            i += 1

        if text2 == "":
            await call.message.answer(f"<b>Afsuski, {date.day}-{OYLAR[date.month]} kuni yakunlanuvchi giveawaylar mavjud emas 🥲</b>", reply_markup=menu.menu)
        else:
            text = f"{date.day}-{OYLAR[date.month]} kuni yakunlanuvchi giveawaylar ro'yxati :\n\n\n"
            text += text2
            text += f"\n\n<i>Kanalimiz : @{CHANNEL_USERNAME}</i>"
            
            text = f"<b>{text}</b>"
            
            await call.message.answer_photo(photo=PREMIUM_PHOTO, caption=text, reply_markup=menu.menu)
        
    await state.clear()
    
@router.message(States.ruyxat)
async def none(msg : Message):
    await msg.delete()
    dm = await msg.answer(
        "<b>👆 Yuqoridagi tugmalardan foydalaning !</b>"
    )
    await asyncio.sleep(3)
    await dm.delete()
