# 🧠 Clarity AI (Local LLM Decision Assistant)

Clarity AI is a lightweight AI-powered decision assistant built using a locally running LLM via Ollama.  

It transforms messy thoughts into structured clarity with actionable guidance.

---

## 🚀 Features

- ✅ Fully local AI (no API cost)
- ✅ Real-time streaming response
- ✅ Structured clarity framework
- ✅ Simple and clean Streamlit interface
- ✅ No external cloud dependency

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ollama (Local LLM Runtime)
- Local Model: phi3:mini / tinyllama
- Requests (HTTP communication)

---

## 🧠 How It Works

1. User enters a confused thought.
2. The app constructs a structured clarity prompt.
3. Streamlit sends request to local Ollama server.
4. The model streams response in real-time.
5. Output is displayed in structured format:

- Core Problem  
- Hidden Fear  
- Logical Breakdown  
- Immediate Next Action  
- What NOT to Do  
- Conclusion  

---

##DEMO:
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/b696ab84-d3cf-4ec1-afb1-c50c33db6d8b" />

## 🏗 System Architecture

User Input  
↓  
Streamlit UI  
↓  
HTTP Request  
↓  
Ollama Local Server  
↓  
LLM (phi3:mini / tinyllama)  
↓  
Streaming Response  
↓  
Rendered Structured Output

## ⚙️ Setup Instructions

### 1️⃣ Install Ollama
Download from:
https://ollama.com

### 2️⃣ Pull Model
