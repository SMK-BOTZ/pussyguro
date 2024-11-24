import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7488363157:AAFIgo_pyqfdP2PohBRRc2iFv6IEt4Rbb7s")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002377004374"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5961139833"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://itzshubham47:2PYWQKkbKGXb7gQx@cluster0.25jkq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002483117711"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI can store private files in Animes Duo Channel and other users can access it from special link. \n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/VR_unreal'>ᴠʀ ᴜɴʀᴇᴀʟ✨</a></b>")
try:
    ADMINS=[6551906246]
    for x in (os.environ.get("ADMINS", "7871556756 6447084129 5961139833 6551906246 6586546549").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ᴛʜᴀɴᴋ ʏᴏᴜ! ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ. ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀɴɪᴍᴇꜱ ꜰɪʟᴇꜱ. ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ꜰɪʟᴇꜱ ᴠɪᴀ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ.\n ○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/Fushiguro_x'>𝐅ᴜsʜɪɢᴜʀᴏ</a> \n ○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Duo'>𝐀ɴɪᴍᴇ 𝐇ɪɴᴅɪ</a> \n ○ 𝐇ᴀɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+rqJjl4BBd3M4NDc1'>𝐇ᴜɴᴛᴀɪ 𝐖ᴏʀʟᴅ</a> \n ○ 𝐃ᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/VR_Necromancer'>ɴᴇᴄʀᴏᴍᴀɴᴄᴇʀ</a> \n ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href='https://t.me/vr_unreal'>ᴠʀ ᴜɴʀᴇᴀʟ</a></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(5961139833)

LOG_FILE_NAME = "unrealshubham.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
