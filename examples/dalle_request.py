import requests
import load_env
import uuid
import os

os.load_env()

# Define the endpoint URL
base_url = "http://localhost:8000"  # Replace with your actual base URL
endpoint = "/v1/images/generations"

# Example request data
request_data = {
    "prompt": "A futuristic cityscape at sunset",
    "n": 1,
    "size": "1024x1024",
    "response_format": "url",
    "user": None
}

api_key = "API_KEY"

# Construct headers with authorization
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Make the POST request
try:
    response = requests.post(base_url + endpoint, json=request_data, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Print the response JSON
    print("Response JSON:")
    print(response.json())

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")

