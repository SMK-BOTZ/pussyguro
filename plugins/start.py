#PoweredBySAHIL

import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

"""Add time in seconds for waiting before delete 
1min = 60, 2min = 60*2 = 120, 5min = 60*5 = 300"""
SECONDS = int(os.getenv("SECONDS", "1500"))

async def send_files(client: Client, user_id: int, ids: list[int], base64_string: str):
    messages = await get_messages(client, ids)
    snt_msgs = []

    # Send files and save reference
    for msg in messages:
        if bool(CUSTOM_CAPTION) & bool(msg.document):
            caption = CUSTOM_CAPTION.format(previouscaption="" if not msg.caption else msg.caption.html, filename=msg.document.file_name)
        else:
            caption = "" if not msg.caption else msg.caption.html

        if DISABLE_CHANNEL_BUTTON:
            reply_markup = msg.reply_markup
        else:
            reply_markup = None

        try:
            snt_msg = await msg.copy(chat_id=user_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
            await asyncio.sleep(0.5)
            snt_msgs.append(snt_msg)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            snt_msg = await msg.copy(chat_id=user_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
            snt_msgs.append(snt_msg)
        except Exception as e:
            print(f"Error: {e}")
            pass

    # Send the notification message about file deletion
    temp_msg = await client.send_message(
        user_id,
        "<b>➢ 𝗙𝗶𝗹𝗲𝘀 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝘂𝘁𝗼 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗜𝗻 25 𝗠𝗶𝗻 🥹⏳️ \n➢ 𝗗𝘂𝗲 𝗧𝗼 𝗔𝘃𝗼𝗶𝗱 𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗜𝘀𝘀𝘂𝗲𝘀 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 & 𝗦𝗮𝘃𝗲 𝗜𝘁 ⚠️</b>"
    )

    # Wait for the specified time
    await asyncio.sleep(SECONDS)

    # Delete files
    for snt_msg in snt_msgs:
        try:
            await snt_msg.delete()
        except Exception as e:
            print(f"Error: {e}")
            pass

    # Delete the initial message
    try:
        await temp_msg.delete()
    except Exception as e:
        print(f"Error: {e}")
        pass

    # Use client.username for dynamic bot username
    retrieve_url = f"https://t.me/{client.username}?start={base64_string}"
    await client.send_message(
        user_id,
        "<b>➢ 𝗙𝗶𝗹𝗲𝘀 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝘂𝘁𝗼 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗜𝗻 25 𝗠𝗶𝗻 🥹⏳️ \n➢ 𝗗𝘂𝗲 𝗧𝗼 𝗔𝘃𝗼𝗶𝗱 𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗜𝘀𝘀𝘂𝗲𝘀 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 & 𝗦𝗮𝘃𝗲 𝗜𝘁 ⚠️</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Rᴇᴛʀɪᴇᴠᴇ Fɪʟᴇꜱ Bᴀᴄᴋ ⚡️", url=retrieve_url)]])
    )

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except Exception as e:
            print(f"Error: {e}")
            pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return

        await send_files(client, message.from_user.id, list(ids), base64_string)
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡️ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("✨ ᴄʟᴏꜱᴇ", callback_data = "close")
                ]
            ]
        )
        picture_url = "https://graph.org/file/6eb635397847d798b231b-9a91ae2772a3fa3ed5.png"
        await client.send_photo(
            chat_id=message.chat.id,
            photo=picture_url,
            caption=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup
        )
        return

@Bot.on_callback_query(filters.regex(r"retrieve_(.+)"))
async def retrieve_files(client: Client, callback_query: CallbackQuery):
    base64_string = callback_query.data.split("_")[1]
    user_id = callback_query.from_user.id

    original_string = await decode(base64_string)
    argument = original_string.split("-")

    if len(argument) == 3:
        try:
            start = int(int(argument[1]) / abs(client.db_channel.id))
            end = int(int(argument[2]) / abs(client.db_channel.id))
        except:
            return
        if start <= end:
            ids = range(start, end + 1)
        else:
            ids = []
            i = start
            while True:
                ids.append(i)
                i -= 1
                if i < end:
                    break
    elif len(argument) == 2:
        try:
            ids = [int(int(argument[1]) / abs(client.db_channel.id))]
        except:
            return

    await callback_query.message.delete()
    await send_files(client, user_id, list(ids), base64_string)

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ¹", url=client.invitelink),
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ²", url="https://t.me/+AgCVNBsS6PA4ZWQ1")
        ],[
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ³", url="https://t.me/Dragon_Ball_in_Hindi_Dubbed_HQ")
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None if not message.from_user.username else '@' + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="Processing ...")
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1

        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""

        return await pls_wait.edit(status)

    else:
        msg = await message.reply("<code>Use this command as a reply to any telegram message without any spaces.</code>")
        await asyncio.sleep(8)
        await msg.delete()
