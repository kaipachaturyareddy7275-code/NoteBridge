from fastapi import FastAPI
import os
from fastapi import UploadFile, File, HTTPException

app = FastAPI(title="NoteBridge")

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.get("/")
def home():
    return {"message": "Welcome to NoteBridge!"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"message": "PDF uploaded successfully", "filename": file.filename}