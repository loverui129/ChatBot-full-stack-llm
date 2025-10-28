from fastapi import FastAPI
from backend.routers import chat,upload
from fastapi.middleware.cors import CORSMiddleware
from backend.database.init_db import init_db  

# Initialize database
init_db()
app = FastAPI() # # Create FastAPI app

# Enable CORS for frontend (React/Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(chat.router, prefix="/chat", tags=["Chat Agent"])
app.include_router(upload.router, prefix="/upload", tags=["File Upload"])

@app.get("/") # Root endpoint
def root(): # Simple health check endpoint
    return {"message": " 🤖 Chatbot API is running"}