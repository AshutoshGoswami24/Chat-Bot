from pyrogram import filters
from main import app  # Import the app object from main.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to generate a response using OpenAI's GPT-3 model
async def generate_response(question):
    try:
        # Generate response using GPT-3
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            temperature=0.7,
            max_tokens=150
        ).choices[0].text.strip()

        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Message handler for the /ask command in Telegram groups
@app.on_message(filters.command(["ask"]) & filters.group)
async def ask_command_group_handler(client, message):
    try:
        # Extract the question from the command
        command_parts = message.text.split(maxsplit=1)
        question = command_parts[1] if len(command_parts) > 1 else ""

        # Generate a response using GPT-3
        answer = await generate_response(question)

        # Reply with the answer
        await message.reply(answer)
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
