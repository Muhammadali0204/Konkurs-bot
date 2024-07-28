import asyncio, logging
from contextlib import suppress
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram.fsm.storage.memory import MemoryStorage

from loader import bot, client
from utils.on_startup import on_startup
from handlers import admin, user, channel
from data.config import ADMINS, BOT_TOKEN

async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(admin.router, user.router, channel.router)
    
    await client.start()
    print("Client has started ✅")
    
    await on_startup(bot)
    await bot(DeleteWebhook(drop_pending_updates=True))
    print("Bot has started ✅")
    await dp.start_polling(bot)
    
    

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main=main())
