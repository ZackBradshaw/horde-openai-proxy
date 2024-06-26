import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_api_base = os.getenv("OPENAI_BASE_URL")
openai_api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

# Initialize the OpenAI client
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# Define the chat messages
messages = [
    {
        "role": "user",
        "content": "Write snake in python",
    },
    # Uncomment for vision
    # {
    #     "role": "user",
    #     "content": {
    #         "type": "image_url",
    #         "image_url": {
    #             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
    #         },
    #     },
    # },
]

# Create chat completion
chat_response = client.chat.completions.create(
    model=model,
    messages=messages,
)

# Print the chat response
print("Chat response:", chat_response)
