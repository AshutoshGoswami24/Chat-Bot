from config import *
from pyrogram import Client, filters

@app.on_message(filters.command("block", prefixes="/") & filters.private)
async def block_command(client, message):
    # Block the user who sent the command
    await client.block_user(message.from_user.id)
    await message.reply("You have been blocked.")

# Define a handler for the /unblock command
@app.on_message(filters.command("unblock", prefixes="/") & filters.private)
async def unblock_command(client, message):
    # Check if user is an admin
    if message.from_user.id in admins:
        # Unblock the user specified in the command
        if len(message.command) > 1:
            try:
                user_id = int(message.command[1])
                await client.unblock_user(user_id)
                await message.reply("User has been unblocked.")
            except ValueError:
                await message.reply("Invalid user ID.")
        else:
            await message.reply("Please specify the user's ID to unblock.")
    else:
        await message.reply("You are not authorized to use this command.")

# Define a handler for all messages
@app.on_message(filters.private)
async def handle_messages(client, message):
    # Check if the message is "/block"
    if message.text.lower() == "/block":
        # Block the user who sent the message
        await client.block_user(message.from_user.id)
        await message.reply("You have been blocked.")
