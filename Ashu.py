from pyrogram import Client, idle
from plugins.main import app as Client2
from config import *



bot = Client(

           "Renamer",

           bot_token=bot_token,

           api_id=api_id,

           api_hash=api_hash,

           plugins=dict(root='plugins'))
           

if I-Am-Ashu:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
