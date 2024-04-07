import os
import asyncio
import random
import psutil
import speedtest
from os import getenv, environ
from pyrogram import Client, filters
from plugins.Ashutosh_Goswami import *   # Importing qa_dict from qur.py
from config import *
from pyrogram.errors import PeerIdInvalid
from aiogram import types
from aiohttp import web
from os import environ
# Create a Pyrogram client

BOT_TOKEN = bot_token

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


print("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠😴......")


welcome_message = "{username} 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗧𝗵𝗲 𝗙𝗮𝗺𝗶𝗹𝘆  😁"
goodbye_message = "𝗚𝗼𝗼𝗱 𝗕𝘆𝗲 {username} 🥺 𝘄𝗲 𝘄𝗶𝗹𝗹 𝗺𝗶𝘀𝘀 𝘆𝗼𝘂"


print("𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝😁......")

