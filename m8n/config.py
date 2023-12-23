# Created By @xl444
# Copyright By watan

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAB70I9bwA6g0NCWID3a_DefS11D4z8zo4CKkjq43ZKOLuUOeAgN6jIQvIygoCyqiqqF-gYuIoguooJB1SHyi27az1BxgQQooXUFDoh6jPKcZpIJlXvJ6NQp-lWCnMRy7iaZvZAnFr7KJ-n9ozY4BffbDW-qnbVRsHz8Io9tCmk5mm8-ueNzmr8Jk4yjYGm15AXHSLAims_tlULo_yWBFczMIzfoGv8ZydGar2qm2Sqd5V36nwdsM56GufFNH82UcOsbXejze3w6uexo1GDL-rZpuNnkaRLqAc6hZeh1Y_f-Qv5Kdhquy-qeHcNoXYRtuHHGkxTEh_YN_BpM7yEhIdP7AAAAAWIm-aQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5576943944:AAGY8cY_uN33juYb19T6in7he7nSKZQCl70")
BOT_NAME = getenv("BOT_NAME", "bot")
BOT_USERNAME = getenv("BOT_USERNAME", "music_Cvbot")
ASSID = int(getenv("ASSID", "2017683587"))
ASSNAME = getenv("ASSNAME", "𝙈𝙐𝙎𝙄𝘾..🎶")
ASSUSERNAME = getenv("ASSUSERNAME", "𝙈𝙐𝙎𝙄𝘾..🎶")

BOT_ID = int(getenv("BOT_ID", "5330986670"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Team-7X/music_X-v")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
OWNER_ID = int(getenv("OWNER_ID", "1854384004"))
UPDATE = getenv("UPDATE", "XQQAQ")
SUPPORT = getenv("SUPPORT", "XQQAQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", ". / ! + - @ # $").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/82681721aaaa05789dae2.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
START_PIC = getenv("START_PIC", "https://telegra.ph/file/82681721aaaa05789dae2.jpg")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/82681721aaaa05789dae2.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/82681721aaaa05789dae2.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/82681721aaaa05789dae2.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/82681721aaaa05789dae2.jpg")
