import shutil
from datetime import datetime
import os
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "file"


def save_file(file: UploadFile) -> str:
    if not file.filename.lower().endswith(("docs", "pdf", "txt", "docx", "xls", "xlsx", "pptx", "json")):
        raise HTTPException(status_code=400, detail="Faqat TXT, PDF yoki DOCS formatidagi rasmlar yuklash mumkin.")

    _, file_extension = os.path.splitext(file.filename)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    unique_filename = f"{timestamp}{file_extension}"
    image_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return unique_filename