import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

api_key = os.getenv("OPENAI_API_KEY")
print("API Key:", api_key)  # Check if the key is loaded correctly
