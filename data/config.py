import environs


env = environs.Env()

env.read_env()
ADMINS = [int(x) for x in  env.list("admins")]
BOT_TOKEN = env.str("bot_token")
BOT_USERNAME = env.str("bot_username")
CHANNEL_USERNAME = env.str("channel_username")
DATABASE_URL = env.str('database_url')
API_ID = int(env.str('api_id'))
API_HASH = env.str('api_hash')

PREMIUM_PHOTO = "AgACAgIAAxkBAAL8XGamsqq719bEFxSfT8uUqhMMvzUmAAIK3zEb2DcoSU-jvV0DHDAbAQADAgADeQADNQQ"

OYLAR = [
    0,
    'yanvar',
    'fevral',
    'mart',
    'aprel',
    'may',
    'iyun',
    'iyul',
    'avgust',
    'sentyabr',
    'oktyabr',
    'noyabr',
    'dekabr',
]
