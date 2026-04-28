import os
import google.generativeai as genai
from PIL import Image

# Load API key from environment (Streamlit Secrets or local .env)
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Set GEMINI_API_KEY.")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)


# ---------------- CHAT MODEL ----------------
def load_chat_model():
    return genai.GenerativeModel("models/gemini-2.0-flash-001")


# ---------------- ASK ANYTHING ----------------
def ask_anything(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash-001")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- EMBEDDINGS ----------------
def get_embeddings(text):
    try:
        result = genai.embed_content(
            model="models/gemini-embedding-2-preview",
            content=text
        )
        return result["embedding"]
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- IMAGE CAPTIONING ----------------
def generate_image_caption(image):
    try:
        model = genai.GenerativeModel("models/nano-banana-pro-preview")
        response = model.generate_content(["Describe this image", image])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"