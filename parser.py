import os
from dotenv import load_dotenv
from litellmParser import *
from transformers import AutoTokenizer

load_dotenv()
models = ["turboderp/Cat-Llama-3-70B-instruct", "MarsupialAI/HelloNurse-11b","Sao10K/Llama-3-8B-Expr1-Stheno-3.2","mistralai/Mistral-7B-Instruct-v0.1", "cognitivecomputations/dolphin-2.6-mistral-7b", "HuggingFaceH4/zephyr-7b-beta"]
# Path to the local configuration file
model = models[0]
access_token = os.getenv("HUGGING_FACE_HUB_TOKEN")


# Load the tokenizer from the local configuration file
tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=access_token, trust_remote_code=True)

# # Define the chat array
chat = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
    {"role": "user", "content": "I'd like to show off how chat templating works!"},
]
#
# # Apply the chat template
# chat_template = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
#
# print(chat_template)
# print("===============")
#
# chat_t = hf_chat_template(model, chat)
# # Print the chat template
# print(chat_t)

def parse_messages(messages):
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    return prompt


s= parse_messages(chat)
print(s)
