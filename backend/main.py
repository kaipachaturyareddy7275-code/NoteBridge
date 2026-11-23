from fastapi import FastAPI
import os
from fastapi import UploadFile, File, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(title="NoteBridge")

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def home():
    return {"message": "Welcome to NoteBridge!"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    filename = os.path.basename(file.filename)
    
    if not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    content = await file.read()

    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Empty file cannot be uploaded")

    if not content.startswith(b"%PDF-"):
        raise HTTPException(status_code=400, detail="Invalid PDF file")

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    name, extension = os.path.splitext(filename)
    count = 1

    while os.path.exists(file_path):
        filename = f"{name}_{count}{extension}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        count += 1

    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "message": "PDF uploaded successfully",
        "filename": filename
    }
    
@app.get("/pdfs")
def get_uploaded_pdfs():

    files = []

    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(".pdf"):
            files.append(filename)

    return {
        "files": files,
        "total": len(files)
    }

@app.get("/pdfs/{filename}")
def view_pdf(filename: str):

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="PDF not found")

    if not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    return FileResponse(
    path=file_path,
    media_type="application/pdf",
    filename=filename,
    content_disposition_type="inline"
    )