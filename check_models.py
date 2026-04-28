import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set GEMINI_API_KEY in .env file")

# Create client
client = genai.Client(api_key=api_key)

# List available models
try:
    models = client.models.list()

    print("Available Models:\n")
    for model in models:
        print(model.name)

except Exception as e:
    print(f"Error: {str(e)}")