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
from CmD import *
from pyrogram.errors import PeerIdInvalid
from aiogram import types
from aiohttp import web
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from os import environ
from pyrogram.errors.exceptions import Forbidden


# Create a Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

print("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠😴......")

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

app.run()
