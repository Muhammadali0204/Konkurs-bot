from aiogram import Bot
from telethon import TelegramClient
from aiogram.client.default import DefaultBotProperties

from data.config import BOT_TOKEN, API_ID, API_HASH

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="html"))
client = TelegramClient(session='data/998330030953', api_id=API_ID, api_hash=API_HASH, device_model="Konkurs bot")
