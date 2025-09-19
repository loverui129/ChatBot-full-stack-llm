from fastapi import FastAPI
from routers import ask,upload
from fastapi.middleware.cors import CORSMiddleware
from database.init_db import init_db

init_db()
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # local
        "https://chatbot-full-stack-llm-frontend.onrender.com"  # render frontend
        "https://chatbot-full-stack-llm.onrender.com",  # backend render
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ask.router,prefix="/ask",tags=["ask"])
app.include_router(upload.router,prefix="/upload",tags=["upload"])

@app.get("/")
def root():
    return {"message": "Chatbot API is running"}
