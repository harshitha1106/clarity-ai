# 🧠 Clarity AI — Local LLM Decision Assistant

Clarity AI is a lightweight AI-powered decision assistant built using a locally running Large Language Model (LLM) via Ollama.

It transforms messy thoughts into structured clarity with actionable guidance.

---

## 🚀 Features

- ✅ Fully local AI (no API cost)
- ✅ Real-time streaming responses
- ✅ Structured clarity framework
- ✅ Clean Streamlit interface
- ✅ No external cloud dependency

---

## 🏗 System Architecture

User Input  
↓  
Streamlit UI  
↓  
HTTP Request  
↓  
Ollama Local Server (127.0.0.1:11434)  
↓  
Local LLM (phi3:mini / tinyllama)  
↓  
Streaming Token Response  
↓  
Rendered Structured Output  

---

## 🧠 How It Works

1. The user enters a confused thought.
2. The app builds a structured clarity prompt.
3. A request is sent to a locally running LLM via Ollama.
4. The model streams tokens in real time.
5. The UI updates progressively as the response is generated.

### Why Streaming?

Initially, non-streaming inference caused timeout issues on low-memory systems because the request waited for full completion.

Switching to streaming enabled token-wise incremental responses, preventing blocking and improving responsiveness.

---

## 📌 Output Format

The assistant responds in this structured format:

- Core Problem  
- Hidden Fear  
- Logical Breakdown  
- Immediate Next Action  
- What NOT to Do  
- Conclusion  

The goal is to provide simple, direct, actionable clarity.

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ollama (Local LLM Runtime)
- Local Model: phi3:mini / tinyllama
- Requests (HTTP communication)

---

## 🖥 Running This Project Locally

### 1️⃣ Install Ollama
Download from:
https://ollama.com

### 2️⃣ Pull Required Model

##DEMO:
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/b696ab84-d3cf-4ec1-afb1-c50c33db6d8b" />


---

## ⚠ Limitations

- Small local models may produce incorrect factual outputs.
- Quality depends on selected model.
- Not intended for production-level deployment.
- Performance depends on system RAM and CPU.

---

## 🌱 Project Context

This is my first hands-on AI systems project.

The goal was not just to use an LLM, but to deeply understand:

- Local model deployment
- Streaming token responses
- Prompt structuring
- Timeout debugging
- Virtual environment management
- Real-time UI updates

This project helped me move from *using AI tools* to *building AI-powered systems*.

---

## 🚀 Future Improvements

- Add conversation memory
- Improve factual reliability
- Add emotion intensity slider
- Improve UI polish
- Explore hybrid local + cloud inference

---

## 👨‍💻 Author

Built as a beginner AI systems project to understand LLM integration and local inference architecture.
