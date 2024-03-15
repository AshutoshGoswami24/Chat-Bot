from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



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
