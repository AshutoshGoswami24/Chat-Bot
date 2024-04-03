import re
import os
from os import getenv, environ

      

api_id = int(environ.get("API_ID", ""))
api_hash = environ.get("API_HASH", "")
ADMINS = int(environ.get("ADMINS", ""))
bot_token = environ.get("BOT_TOKEN", "")
PICS = (environ.get('PICS', '')).split()
I-Am-Ashu = (environ.get('I-Am-Ashu', 'True')).split()
START_TXT = """<b>𝐇𝐞𝐥𝐥𝐨 {}, ɪ ᴀᴍ {},ɪ ᴀᴍ ᴀ ᴄʜᴀᴛʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴘᴀɴᴅᴀᴡᴇʙ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ, ᴛʜᴇɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ᴀs ᴀ ғʀɪᴇɴᴅ. 😊 [𝙈𝙮 𝘾𝙝𝙖𝙣𝙣𝙖𝙡](https://t.me/Pandawep)</b>"""
ALL_TXT = """<b>𝐇𝐞𝐥𝐥𝐨 {}, 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐦𝐲 𝐚𝐥𝐥 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐛𝐨𝐭𝐬. 🤖</b>"""
