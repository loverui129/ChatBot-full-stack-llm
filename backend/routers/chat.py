from fastapi import APIRouter
from pydantic import BaseModel
from services.agent_service import run_agent

# Initialize router
router = APIRouter()

# Request body model
class ChatRequest(BaseModel):
    question: str

# Main chat endpoint
@router.post("/")
async def chat(request: ChatRequest): # accept NLP-> The agent automatically determines and calls the appropriate tool
    user_question = request.question
    answer = run_agent(user_question)
    return {"question": user_question, "answer": answer}
