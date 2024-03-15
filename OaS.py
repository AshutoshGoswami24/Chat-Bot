from config import *
from main import *
from pyrogram import Client, filters

from pyrogram import Client, filters
from datetime import datetime, timedelta

# Define your function to ban a user based on a reply
async def ban_user(client, message):
    try:
        # Check if the message text contains the /ban command
        if "/ban" in message.text:
            # Ensure the user has replied to a message
            if not message.reply_to_message:
                await message.reply_text("Please reply to a message to ban the user.")
                return
            
            # Extract the user ID from the replied message
            user_id_to_ban = message.reply_to_message.from_user.id
            chat_id = message.chat.id
            
            # Ban the user
            await client.kick_chat_member(chat_id, user_id_to_ban)
            await message.reply_text("User banned successfully!")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
    else:
        await message.reply("You are not authorized to use this command.")

# Start the Pyrogram client
app.run()
