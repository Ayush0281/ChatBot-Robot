import os
import google.generativeai as genai
from PIL import Image

# Load API key from environment
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Set GEMINI_API_KEY in Streamlit Secrets.")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)


# ---------------- CHAT MODEL ----------------
def load_chat_model():
    return genai.GenerativeModel("gemini-pro")


# ---------------- ASK ANYTHING ----------------
def ask_anything(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- EMBEDDINGS ----------------
def get_embeddings(text):
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content=text
        )
        return result["embedding"]
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- IMAGE CAPTIONING ----------------
def generate_image_caption(image):
    try:
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content(["Describe this image", image])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"