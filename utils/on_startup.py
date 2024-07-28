from aiogram import Bot, types
from data.config import ADMINS

async def on_startup(bot : Bot):
    await bot.set_my_commands(
        commands=[
            types.BotCommand(command='start', description='Botni ishga tushurish')
        ]
    )
    
    for admin in ADMINS:
        try :
            await bot.send_message(admin, "<b>Bot ishga tushdi</b>")
        except :
            pass