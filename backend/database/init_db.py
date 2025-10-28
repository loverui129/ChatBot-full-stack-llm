# backend/database/init_db.py
from backend.database.connection import Base, engine
from backend.models.document import Document 

def init_db():
    Base.metadata.create_all(bind=engine)
