import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import (
    load_chat_model,
    ask_anything,
    get_embeddings,
    generate_image_caption
)
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Gemini AI App",
    page_icon="🧠",
    layout="centered"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        menu_title="Gemini AI",
        options=["ChatBot", "Image Captioning", "Embeddings", "Ask Me Anything"],
        icons=["chat-dots-fill", "image-fill", "textarea-t", "patch-question-fill"],
        menu_icon="robot",
        default_index=0
    )

# ---------------- LOAD CLIENT ----------------
client = load_chat_model()

# ---------------- SESSION STATE ----------------
if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-3.1-flash-lite-preview"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# 🤖 CHATBOT
# =========================================================
if selected == "ChatBot":

    st.title("🤖 Gemini ChatBot")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_prompt = st.chat_input("Ask something...")

    if user_prompt:

        st.chat_message("user").markdown(user_prompt)

        st.session_state.messages.append({
            "role": "user",
            "content": user_prompt
        })

        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_session.send_message(user_prompt)
                reply = response.text
            except Exception:
                reply = "Something went wrong. Try again."

        with st.chat_message("assistant"):
            st.markdown(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_session = client.chats.create(
            model="gemini-3.1-flash-lite-preview"
        )

# =========================================================
# 🖼️ IMAGE CAPTIONING
# =========================================================
elif selected == "Image Captioning":

    st.title("🖼️ Image Captioning")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        if st.button("Generate Caption"):
            with st.spinner("Analyzing image..."):
                caption = generate_image_caption(image)

            st.success("Caption:")
            st.write(caption)

# =========================================================
# 🔤 EMBEDDINGS
# =========================================================
elif selected == "Embeddings":

    st.title("🔤 Text Embeddings")

    text = st.text_area("Enter text")

    if st.button("Generate Embeddings"):
        if text.strip():
            with st.spinner("Processing..."):
                embeddings = get_embeddings(text)

            st.success("Embeddings Generated")
            st.write(embeddings)
        else:
            st.warning("Please enter text")

# =========================================================
# ❓ ASK ME ANYTHING
# =========================================================
elif selected == "Ask Me Anything":

    st.title("❓ Ask Me Anything")

    prompt = st.text_area("Enter your question")

    if st.button("Get Answer"):
        if prompt.strip():
            with st.spinner("Thinking..."):
                answer = ask_anything(prompt)

            st.success("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question")