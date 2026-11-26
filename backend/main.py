from fastapi import FastAPI
import os
from fastapi import UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi import Response
from backend.database import create_tables
from backend.database import insert_document
from backend.database import get_all_documents
from backend.database import update_document
from backend.database import delete_document

app = FastAPI(title="NoteBridge")

create_tables()

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
        
    insert_document(filename, file_path)

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
    
@app.delete("/pdfs/{filename}")
def delete_pdf(filename: str):

    filename = os.path.basename(filename)

    if not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files can be deleted")

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="PDF not found")

    os.remove(file_path)

    return {
        "message": "PDF deleted successfully",
        "filename": filename
    }
    
@app.get("/documents")
def get_documents_from_database():
    documents = get_all_documents()

    return {
        "documents": documents,
        "total": len(documents)
    }
    
@app.put("/documents/{document_id}")
def update_document_details(document_id: int, new_filename: str):

    updated = update_document(document_id, new_filename)

    if not updated:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "message": "Document updated successfully",
        "document_id": document_id,
        "new_filename": new_filename
    }
    
@app.delete("/documents/{document_id}")
def delete_document_details(document_id: int):

    deleted = delete_document(document_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "message": "Document deleted successfully",
        "document_id": document_id
    }