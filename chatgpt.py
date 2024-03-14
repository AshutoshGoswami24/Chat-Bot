import openai



# Function to generate a response using OpenAI's GPT-3 model
async def generate_response(question):
    try:
        # Generate response using ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            temperature=0.7,
            max_tokens=150
        ).choices[0].text.strip()

        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"
