## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgByv4Fk048-B-liO4m78_j1AWb8mlhBRlO9KL3JcOesN4VashHUHxNEi9pO-VCXzfbdQpEUGCp2utbyahOIknI1LiJtfec-PWhpHInsvfUvz7JG3pEWlL4fyjPoBHHX1Cibd7zSVTMlmoRu3XNs7c6k9eFzvwqUvp1dxSGv0aakTqj7JlAm2umz2ga2psbVeyKksReGe9Ercr1zXO6fUSmpux52ONcWAs10JfnTo41LZ8Bujg5Tgj5G89KV6nQFT4MalmHfF7HeEO8XGnri0xtHeZVp-VgX-KRjtzaQB8TiHOeL723gpAf6Bn5_dU_vy2acwxLRGtfIcd65Sl0zU_M1AAAAATkAKpQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5182584060:AAFcjB1qIQQ9_n_JK3W5FHHKd_hNR6cHsFY")
BOT_NAME = getenv("BOT_NAME", "20 music")
API_ID = int(getenv("API_ID", "11667194"))
API_HASH = getenv("API_HASH", "d9d35aba2f380f414a3aae53565b3334")
OWNER_NAME = getenv("OWNER_NAME", "alsh al sultan")
OWNER_USERNAME = getenv("OWNER_USERNAME", "aaaoao")
ALIVE_NAME = getenv("ALIVE_NAME", "alsh al sultan")
BOT_USERNAME = getenv("BOT_USERNAME", "ii1ilBoT")
OWNER_ID = getenv("OWNER_ID", "1660459490")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "II1IlIbot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "aaaoao")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tttsst")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1660459490").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
