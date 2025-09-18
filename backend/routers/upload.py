from fastapi import APIRouter,UploadFile,File,Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from models.document import Document
import os

from langchain_core import vectorstores
from services.file_service import parse_file

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores import FAISS

router = APIRouter()
UPLOAD_DIR = "uploads"
VECTOR_DIR = "vectorstore"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# databse session 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
     file_path = os.path.join(UPLOAD_DIR, file.filename)
     with open(file_path, "wb") as f:
          f.write(await file.read())

    # 2. save databse
     db_doc = Document(filename=file.filename, filepath=file_path)
     db.add(db_doc)
     db.commit()
     db.refresh(db_doc)

     # split file
     content = parse_file(file_path)
     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
     docs = splitter.split_text(content)

     # embeddings
     embeddings = OpenAIEmbeddings()
     vectorstore = FAISS.from_texts(docs, embedding=embeddings)

     # save to faiss
     vectorstore.save_local(VECTOR_DIR)
     
     return {"id": db_doc.id,
             "filename": file.filename,
             "message": "File uploaded successfully",
             "chunks": len(docs)}