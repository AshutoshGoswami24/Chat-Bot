from config import *
from pyrogram import Client, filters

async def send_message_to_admins(message):
    for admin_id in admins:
        await app.send_message(admin_id, message)
        
# Define a handler for the /start command
@app.on_message(filters.private & filters.command(["st"]))
async def start_command(client, message):
    me = await app.get_me()
    await message.reply("Welcome to the bot!")

    # Check if the user is an admin
    if message.from_user.id in admins:
        # Get the user ID from the command
        if len(message.command) > 1:
            user_id = int(message.command[1])

            # Block the user
            await app.block_user(user_id)
            await message.reply(f"User {user_id} has been blocked.")

            # Notify admins about the action
            await send_message_to_admins(f"Admin {message.from_user.id} has blocked user {user_id}.")
        else:
            await message.reply("Please specify the user's ID to block.")
    else:
        await message.reply("You are not authorized to use this command.")

# Start the Pyrogram client
app.run()
