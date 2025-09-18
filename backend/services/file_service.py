import os
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document

def parse_file(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lower()
    text = ""

    if extension == ".pdf":
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    
    elif extension == ".docx":
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

    elif extension == ".csv":
        df=pd.read_csv(file_path)
        text = df.to_string()

    else:
        raise ValueError(f"Unsupported file extension: {extension}")
    
    return text