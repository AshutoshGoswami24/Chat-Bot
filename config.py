import re
import os
from os import getenv, environ
api_id = int(environ.get("API_ID", ""))
api_hash = environ.get("API_HASH", "")
ADMINS = int(environ.get("ADMINS", ""))
bot_token = environ.get("BOT_TOKEN", "")
PICS = (environ.get('PICS', '')).split()
OPENAI_API_KEY = environ.get("OPENAI_API_KEY", "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")
