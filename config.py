import re
import os
from os import getenv, environ

      

API_ID = int(environ.get("API_ID", "29917436"))
API_HASH = environ.get("API_HASH", "4a926822b076a086a167fe8f2701d3e9")
ADMINS = int(environ.get("ADMINS", "6141937812"))
BOT_TOKEN = environ.get("BOT_TOKEN", "7000509878:AAGseZORtAvEKwuHiESBV1u6E0oCkVq8RFQ")
PICS = (environ.get('PICS', 'https://graph.org/file/7bf517f440a124dc68d80.jpg https://graph.org/file/c42f1ed5e9e9f134b9ddc.jpg https://graph.org/file/a24f0b32ead8fde3adc21.jpg https://graph.org/file/a89bd2adf24a1b1f77bab.jpg https://graph.org/file/80f5cbdf1a7c47e77b490.jpg')).split()

