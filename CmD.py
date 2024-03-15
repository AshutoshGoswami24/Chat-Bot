import random

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters

from main import app

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

