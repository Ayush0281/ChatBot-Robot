# 🤖 Gemini AI Chatbot (Streamlit App)

🚀 **Live Demo:** https://chatbot-robot-juyhipghsat2ffhfnbuk3b.streamlit.app/

An AI-powered multi-functional web application built using **Python, Streamlit, and Google Gemini API**.  
Developed as part of a **Summer Training Project at IIT Kanpur**.

---

## 🚀 Features

- 💬 **AI Chatbot** – Real-time conversational AI using Gemini
- 🖼️ **Image Captioning** – Generate captions for uploaded images
- 🔤 **Text Embeddings** – Convert text into vector embeddings
- ❓ **Ask Me Anything** – General-purpose AI responses
- 🔑 **User API Key Support** – Users can optionally use their own Gemini API key

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Google Gemini API  
- **Libraries:**
  - streamlit
  - google-generativeai
  - pillow
  - python-dotenv

---

## 📂 Project Structure
project/
│── main.py # Streamlit UI
│── gemini_utility.py # Gemini API logic
│── requirements.txt # Dependencies
│── .env # API key (excluded)
│── .gitignore
│── README.md


---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repository

git clone https://github.com/Ayush0281/ChatBot-Robot.git

cd ChatBot-Robot


### 2. Install dependencies

pip install -r requirements.txt


### 3. Create `.env` file

GEMINI_API_KEY=your_api_key_here


### 4. Run the app

streamlit run main.py


---

## 📸 Screenshots

_Add your project screenshots below:_

### 🔹 Chatbot Interface  
<img width="1920" height="876" alt="ChatBot-UI" src="https://github.com/user-attachments/assets/670765bf-fc6e-4397-a8f2-d6766d2b1077" />

### 🔹 Chatbot Interface  
<img width="1920" height="872" alt="ChatBot-response" src="https://github.com/user-attachments/assets/0ed259df-290b-48e3-9e0f-082e65d0b69b" />

### 🔹 Image Captioning  
<img width="1920" height="877" alt="Image-Captioning-01" src="https://github.com/user-attachments/assets/bfa0218f-14d7-4742-8749-27399e021f3c" />


### 🔹 Image Captioning  
<img width="1920" height="876" alt="Image-Captioning-02" src="https://github.com/user-attachments/assets/90e5e40b-0549-4d6b-8f87-1e52091edea8" />


### 🔹 Embeddings Output 
<img width="1920" height="872" alt="Text-Embeddings" src="https://github.com/user-attachments/assets/2f4e8262-8983-4ea8-985d-01b6c7768323" />



---

## 🔐 Security

- API keys are stored using environment variables  
- `.env` is excluded via `.gitignore`  
- No sensitive data is exposed in the repository  

---

## 🌐 Deployment

This app is deployed using **Streamlit Cloud**.

👉 You can deploy it yourself by:
1. Forking the repo  
2. Adding your API key in Streamlit Secrets  
3. Deploying via Streamlit Cloud  

---

## 📜 Project Details

- Developed at IIT Kanpur Summer Project
- Focused on **Generative AI + Full Stack Integration**  
- Demonstrates real-world usage of LLM APIs  

---

## 🚀 Future Improvements

- Voice-based interaction  
- Chat history storage  
- Multi-language support  
- Database integration  

---

## 👨‍💻 Author

**Sarthak Rana**

- GitHub: https://github.com/Ayush0281  
- LinkedIn: https://linkedin.com/in/sarthak-rana-94894632a
