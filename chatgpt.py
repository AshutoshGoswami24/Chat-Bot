import openai
from config import OPENAI_API_KEY

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

@app.on_message(filters.command(["ask"]))
async def ask_question(client, message):
    try:
        # Prompt the user for a question
        await message.reply("Please enter your question.")

        # Wait for the user's response
        response = await app.listen(filters.text)

        # Generate a response using GPT-3
        question = response.text.strip()
        answer = await generate_response(question)

        # Send the response to the user
        await message.reply(answer)
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
