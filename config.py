import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7340328039:AAEg-qdRoEE6SCegq7UES7KM56mYnXY2JiQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002000189850"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6668627674"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://madarazbotz:BqCSRNckrgPCgGe3@cluster0.6vs4k8q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002178219823"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b> 𝗛𝗲𝘆 , {mention} ✨️ \n\n𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗧𝗲𝗮𝗺 𝗟𝗲𝗴𝗲𝗻𝗱 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 ❤️⚡️ \n━━━━━━━━━━━ ☆ ━━━━━━━━━━━ \n➥ 𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝘀 𝗙𝗿𝗲𝗲 𝗦𝘁𝘂𝗱𝘆 𝗠𝗮𝘁𝗲𝗿𝗶𝗮𝗹𝘀 📚 \n𝗙𝗼𝗿 𝗡𝗘𝗘𝗧 , 𝗝𝗘𝗘 , 𝗕𝗢𝗔𝗥𝗗𝗦 & 𝗖𝗨𝗘𝗧 🔥 \n━━━━━━━━━━━ ☆ ━━━━━━━━━━━ \n➥ 𝗜𝗙 𝗨 𝗟𝗶𝗸𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 , 𝗠𝘂𝘀𝘁 𝗦𝗵𝗮𝗿𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 👀❤️ #𝗧𝗘𝗔𝗠_𝗟𝗘𝗚𝗘𝗡𝗗_𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 ⚜️ \n━━━━━━━━━━━ ☆ ━━━━━━━━━━━ \n➥ 𝗠𝗮𝗱𝗲 𝗕𝘆 ➤ @Itz_Shixnu 🥤 \n➥ 𝗠𝘂𝘀𝘁 𝗝𝗼𝗶𝗻 ➤ @TeamLegend_Backup ✨️ \n ━━━━━━━━━━━ ☆ ━━━━━━━━━━━</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5340652544").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʏ ! {first}<b> \n\nDᴜᴇ Tᴏ Oᴠᴇʀʟᴏᴀᴅ Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙꜱᴄʀɪʙᴇʀ Cᴀɴ Uꜱᴇ Tʜɪs Bᴏᴛ Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟ Tᴏ Uꜱᴇ Mᴇ 🌚⚡️ \n\nKɪɴᴅʟʏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ ❤️👍🏻</b>")

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
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
