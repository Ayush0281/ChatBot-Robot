import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please set GEMINI_API_KEY in .env file")

# Create client
client = genai.Client(api_key=GOOGLE_API_KEY)


# ---------------- CHAT MODEL ----------------
def load_chat_model():
    return client


# ---------------- ASK ANYTHING ----------------
def ask_anything(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- EMBEDDINGS ----------------
def get_embeddings(text):
    try:
        response = client.models.embed_content(
            model="gemini-embedding-2-preview",
            contents=text
        )
        return response.embeddings[0].values
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- IMAGE CAPTIONING ----------------
def generate_image_caption(image):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=[
                "Describe this image in detail",
                image
            ]
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"