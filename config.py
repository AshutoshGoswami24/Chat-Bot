import re
import os
from os import getenv, environ

      

api_id = int(environ.get("API_ID", ""))
api_hash = environ.get("API_HASH", "")
ADMINS = int(environ.get("ADMINS", ""))
bot_token = environ.get("BOT_TOKEN", "")
PICS = (environ.get('PICS', '')).split()

