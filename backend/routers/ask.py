from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import ask_llm

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


router = APIRouter()
VECTOR_DIR = "vectorstore"


class AskRequest(BaseModel):
    question: str

@router.post("/")
async def ask(request: AskRequest):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(VECTOR_DIR, embeddings, allow_dangerous_deserialization=True)

    # retrieve folder from FAISS
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(request.question)
    context = "\n".join([doc.page_content for doc in docs])
    
    # get answers from FAISS and creat new prompt
    prompt = f"Answer the question based on the following context：\n\n{context}\n\nQuestion：{request.question}"

     # GPT analyze it new prompt
    answer = ask_llm(prompt)
    
    #return answer
    return {"answer": answer, "context": context[:200]}