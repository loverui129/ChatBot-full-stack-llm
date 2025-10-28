from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from models.document import Document
import os
from langchain_core import vectorstores
from services.file_service import parse_file
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


router = APIRouter() # 创建api 
UPLOAD_DIR = "uploads"
VECTOR_DIR = "vectorstore"
os.makedirs(UPLOAD_DIR, exist_ok=True)
# databse session 
def get_db(): # 数据库会话 
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
@router.post("/") # endpoint,处理上传的files
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):# depends:在执行 upload_file 这个函数前，先运行 get_db()
     file_path = os.path.join(UPLOAD_DIR, file.filename) #把前端上传的文件保存在本地 uploads/文件夹
     with open(file_path, "wb") as f: #文件写入,二进制
          f.write(await file.read()) # 是异步读取上传文件内容

    # save databse SQLAlchemy ORM 理念
     db_doc = Document(filename=file.filename, filepath=file_path) # 保存文件到数据库
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
