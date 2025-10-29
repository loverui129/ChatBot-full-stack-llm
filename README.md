# 💬 AI Chatbot Full Stack LLM Web Platform


A full-stack AI chatbot web platform built with **FastAPI**, **React (Vite)**, and **LangChain**, containerized with **Docker** and deployed to **Render**.  
The chatbot is powered by **LangChain Agents** and can intelligently select and call **six specialized tools** based on user intent — extending its capability far beyond normal conversation.

---

## 🧰 Available Tools

| 🧠 Tool | ⚙️ Function |
|----------|-------------|
| 🔍 **Web Search** | Performs real-time web search and returns top 3 Google results. |
| 📰 **News Tool** | Fetches latest financial, tech, or industry headlines. |
| 💰 **Stock Price Tool** | Retrieves live stock prices (e.g., NVDA, AAPL, TSLA). |
| 🌤️ **Weather Tool** | Gets current weather info for any city (by name or coordinates). |
| 🌐 **Translate Tool** | Translates between English and Chinese (multi-language supported). |
| ➗ **Calculator** | Performs arithmetic operations (add, subtract, multiply, divide, percentage). |

---

## 🚀 Live Demo
- **Frontend (React):** [https://chatbot-frontend.onrender.com](https://chatbot-frontend.onrender.com)
- **Backend (FastAPI):** [https://chatbot-backend.onrender.com](https://chatbot-backend.onrender.com)

> 🌐 The frontend is fully integrated with the backend API via environment variables.

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React + TypeScript + Vite |
| **Backend** | FastAPI (Python 3.11) |
| **AI Logic** | LangChain + OpenAI API |
| **Database** | PostgreSQL (via Render) |
| **Vector Search** | FAISS |
| **Deployment** | Docker + Render (Static Site + Web Service) |

---

## ⚙️ Features
✅ Conversational chatbot with context memory  
✅ File upload support (PDF, DOCX, TXT)  
✅ Text parsing and embedding with LangChain  
✅ Real-time communication between React frontend and FastAPI backend  
✅ Deployed on Render with CI/CD from GitHub  



