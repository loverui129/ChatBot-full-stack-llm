## 🤖 ChatBot Full-Stack LLM

A full-stack AI chatbot application built with FastAPI (backend) and React + Vite (frontend), powered by PostgreSQL for persistence and integrated with the OpenAI API for intelligent responses.

The project demonstrates modern full-stack + LLM integration, including backend API development, frontend UI, database connection, containerization with Docker, and deployment to the cloud (Render).

## ✨ Features
    
    🔹 Backend: FastAPI with REST endpoints (/ask, /upload)
    
    🔹 Frontend: React + Vite with interactive chatbot UI
    
    🔹 Database: PostgreSQL (hosted on Render) for persistence
    
    🔹 AI Integration: OpenAI API for chatbot responses
    
    🔹 Deployment: Dockerized setup with cloud deployment via Render
    
    🔹 CI/CD: GitHub Actions pipeline for automated build & deploy

## 🛠️ Tech Stack

    Frontend: React + Vite + TailwindCSS
    
    Backend: FastAPI + Python
    
    Database: PostgreSQL + FAISS
    
    AI Layer: OpenAI API
    
    Infrastructure: Docker, Render(Cloud Deployment), GitHub Actions

## 🚀 How to Run the Project

Option 1: Try Live Demo on Render

    Frontend: https://chatbot-full-stack-llm-frontend.onrender.com
    
    Backend: https://chatbot-full-stack-llm.onrender.com


Option 2: Run Locally with Docker Compose

1.Clone the repo:

    git clone https://github.com/loverui129/ChatBot-full-stack-llm.git
    
    cd ChatBot-full-stack-llm

2.Create a .env file in the root directory:

    OPENAI_API_KEY=your_api_key_here
    
    POSTGRES_USER=postgres
    
    POSTGRES_PASSWORD=your_password
    
    POSTGRES_DB=chatbot

3.Start the services with Docker Compose:
    
    docker-compose up --build

4.Visit the app:

    Frontend: http://localhost:5173
    
    Backend: http://localhost:8000





    
