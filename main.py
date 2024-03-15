import os
import asyncio
import random
import psutil
from datetime import datetime, timedelta
from aiogram import types
from os import getenv, environ
from pyrogram import Client, filters
from Ashutosh_Goswami import *   # Importing qa_dict from qur.py
from config import *  # Importing variables from config.py
from OaS import * 
from pyrogram.errors import PeerIdInvalid
from aiogram import types
from aiohttp import web
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from os import environ
from pyrogram.errors.exceptions import Forbidden


# Create a Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

print("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠😴......")


#start&all cmd 
START_TXT = """<b>𝐇𝐞𝐥𝐥𝐨 {}, ɪ ᴀᴍ {},ɪ ᴀᴍ ᴀ ᴄʜᴀᴛʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴘᴀɴᴅᴀᴡᴇʙ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ, ᴛʜᴇɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ᴀs ᴀ ғʀɪᴇɴᴅ. 😊 [𝙈𝙮 𝘾𝙝𝙖𝙣𝙣𝙖𝙡](https://t.me/Pandawep)</b>"""
ALL_TXT = """<b>𝐇𝐞𝐥𝐥𝐨 {}, 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐦𝐲 𝐚𝐥𝐥 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐛𝐨𝐭𝐬. 🤖</b>"""

@app.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('😎Main Channal 😎', url='https://t.me/pandawep')
    ],[
        InlineKeyboardButton('❤️ Chat Family ❤️', url='https://t.me/PandaWepChat')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    me2 = (await client.get_me()).mention
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_TXT.format(message.from_user.mention, me2),
        reply_markup=reply_markup
    )

print("START MASSAGE BUTTON OR FUNCTION Check🟢......")
# Handler for /all command
@app.on_message(filters.command("all") & filters.incoming)
async def all_command(client, message):
    buttons = [
        [
            InlineKeyboardButton('😎Main Channal 😎', url='https://t.me/pandawep')
        ],
        [
            InlineKeyboardButton('⭐️ File To Url Bot ⭐️', url='https://t.me/FileToUrlX_Bot'),
            InlineKeyboardButton('🏧 Auto Rename Bot 🏧', url='https://t.me/AutoRenamePro_bot')
        ],
        [
            InlineKeyboardButton('🔽 All Save Bot 🔽', url='https://t.me/AllSaveBot_bot'),
            InlineKeyboardButton('📝 File Rename Bot 📝', url='https://t.me/FileRenameXBot_bot')
        ],
        [
            InlineKeyboardButton('🍿 Movie Channel 🍿', url='https://t.me/MoviePandaWep'),
            InlineKeyboardButton('🎬 Movie Group 🎬', url='https://t.me/PandaMovieREQ')
        ],
        [
            InlineKeyboardButton('🉐 Hindi Anime 🉐', url='https://t.me/AnimePandaWep'),
            InlineKeyboardButton('👶 Cartoon 👶', url='https://t.me/CTPandaWep')
        ],
        [
            InlineKeyboardButton('🎞️ Webseries 🎞️', url='https://t.me/WebSerisePandaWep'),
            InlineKeyboardButton('📚 Books And Free Course 📚', url='https://t.me/BooksPandaWep')
        ],
        [
            InlineKeyboardButton('📱 Mod Apps 📱', url='https://t.me/ApkAshuModKing24'),
            InlineKeyboardButton('🦸‍♂️ Marvel & DC All 🦸‍♀️', url='https://t.me/MarvelXDcAll')
        ],
        [
            InlineKeyboardButton('❤️ Chat Family ❤️', url='https://t.me/PandaWepChat'),
            InlineKeyboardButton('🎬 PandaFilter Bot 🎬', url='https://t.me/PandaFilter_bot')
        ] 
        ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    me2 = (await client.get_me()).mention
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=ALL_TXT.format(message.from_user.mention, me2),
        reply_markup=reply_markup)

print("ALL MASSAGE BUTTON OR FUNCTION Check🟢......")
#ban or unban

async def is_admin(bot, chat_id, user_id):
    try:
        chat_member = await bot.get_chat_member(chat_id, user_id)
        return chat_member.is_chat_admin()
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

  #ban 



@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure i have met him before.")
    except IndexError:
        return await message.reply("This might be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is already banned\nReason: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"Successfully banned ! Sudhrr ja babu {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("This might be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Successfully unbanned ! Sudhrr ja babu {k.mention}")








#systum-info


# Define a function to send a message to all admins
async def send_message_to_admins(message):
    for admin_id in ADMINS:
        await app.send_message(admin_id, message)
print("ADMINE FXD Check🟢......")
@app.on_message(filters.private & filters.command(["st"]))
async def start_command(client, message):
    me = await app.get_me()

    # Gather system information
    ram = psutil.virtual_memory()
    ram_total = ram.total // (1024 ** 3)  # Convert to GB
    ram_used = ram.used // (1024 ** 3)  # Convert to GB
    ram_free = ram.free // (1024 ** 3)  # Convert to GB
    cpu = psutil.cpu_percent()
    disk = psutil.disk_usage('/')
    disk_total = disk.total // (1024 ** 3)  # Convert to GB
    disk_used = disk.used // (1024 ** 3)  # Convert to GB

    st = speedtest.Speedtest()
    st.download()
    st.upload()
    download_speed = st.results.download / (1024 ** 2)  # Convert to Mbps
    upload_speed = st.results.upload / (1024 ** 2)  # Convert to Mbps
    server = st.get_best_server()

    # Construct the startup message with system information
    system_info = (
        f"Bot started!\n\n"
        f"**System Information:**\n"
        f"RAM Total: {ram_total} GB\n"
        f"RAM Used: {ram_used} GB\n"
        f"RAM Free: {ram_free} GB\n"
        f"CPU Usage: {cpu}%\n"
        f"Disk Total: {disk_total} GB\n"
        f"Disk Used: {disk_used} GB\n"
        f"Download Speed: {download_speed:.2f} Mbps\n"
        f"Upload Speed: {upload_speed:.2f} Mbps\n"
        f"Server Location: {server['host']} ({server['country']})\n"
    )

    # Send the startup message
    await message.reply_text(f"__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__\n{system_info}")
print("SYSTUM INFO Check🟢......")

        
#welcome and exit msg
welcome_message = "{username} 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗧𝗵𝗲 𝗙𝗮𝗺𝗶𝗹𝘆  😁"
goodbye_message = "𝗚𝗼𝗼𝗱 𝗕𝘆𝗲 {username} 🥺 𝘄𝗲 𝘄𝗶𝗹𝗹 𝗺𝗶𝘀𝘀 𝘆𝗼𝘂"

#Dont-cng-in-this

print("WELCOME AND GOOD BYE MSG Check🟢......")
# Function to handle messages in groups or channels
@app.on_message(filters.group & (filters.text | filters.command))
async def handle_message(client, message):
    text = message.text.lower()

    # Send the response from qa_dict as a new message
    if text in qa_dict:
        response = qa_dict[text]
        # Replace {username} with the actual username if available
        if "{username}" in response:
            if message.from_user.username:
                username = "@" + message.from_user.username
                response = response.replace("{username}", username)
            else:
                response = response.replace("{username}", "this user")
        await message.reply(response)

print("QRD TXT AND FUNCTION Check ALL OF AND NEX......") 

@app.on_message(filters.group & filters.new_chat_members)
async def handle_new_chat_members(client, message):
    for new_member in message.new_chat_members:
        username = new_member.username
        if username:
            response = welcome_message.format(username="@" + username)
            await message.reply_text(response)
        else:
            response = welcome_message.format(username="this new member")
            await message.reply_text(response)

print("NEW MEMBERT QRD Check🟢......")

@app.on_message(filters.group & filters.left_chat_member)
async def handle_left_chat_member(client, message):
    user_info = message.left_chat_member
    if user_info.username:
        response = goodbye_message.format(username="@" + user_info.username)
        await message.reply_text(response)
    else:
        response = goodbye_message.format(username="this user")
        await message.reply_text(response)

print("𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝😁......")

# Start the bot
app.run()
