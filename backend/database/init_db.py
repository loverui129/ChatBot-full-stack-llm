# backend/database/init_db.py
from database.connection import Base, engine
from models.document import Document 

def init_db():
    Base.metadata.create_all(bind=engine)
