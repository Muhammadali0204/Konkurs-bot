from aiogram import types, Router,enums, F

from loader import bot
from models.models import session, User
from data.config import ADMINS
from keyboards.inline import admin


router = Router()
router.message.filter(F.from_user.id.in_(ADMINS), F.chat.type == enums.chat_type.ChatType.PRIVATE)
router.callback_query.filter(F.from_user.id.in_(ADMINS), F.message.chat.type == enums.chat_type.ChatType.PRIVATE)
    

@router.message(F.text.lower() == "admin")
async def func(msg : types.Message):
    await msg.answer("<b>Admin panel</b>", reply_markup=admin.panel)

@router.callback_query(F.data == "soni")
async def soni(call : types.CallbackQuery):
    n = session.query(User).all().count()
    await call.answer(f"Foydalanuvchilar soni : {n} ta", show_alert=True)
        