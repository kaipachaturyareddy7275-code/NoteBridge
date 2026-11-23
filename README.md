# NoteBridge 📚

NoteBridge is a document management application that allows users to upload, manage, and access PDF documents. It is being developed using Python and FastAPI.

## Features

- Upload PDF documents.
- Validate uploaded files.
- Reject empty and invalid PDF files.
- Prevent overwriting files with duplicate filenames.
- View the list of uploaded PDF documents.
- Retrieve and view uploaded PDFs.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- REST API
- Git and GitHub

## Project Structure

```text
NoteBridge/
│
├── backend/
│   └── main.py
│
├── uploads/
│   └── Uploaded PDF files
│
├── venv/
│
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/upload` | Upload a PDF document |
| GET | `/pdfs` | List all uploaded PDF documents |
| GET | `/pdfs/{filename}` | Retrieve/view a specific PDF |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd NoteBridge
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```powershell
.\venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn python-multipart
```

### 5. Run the Application

```bash
uvicorn backend.main:app --reload
```

### 6. Access the API

Application:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

## Usage

- Use the `/upload` endpoint to upload PDF documents.
- Use the `/pdfs` endpoint to retrieve the list of uploaded documents.
- Use `/pdfs/{filename}` to retrieve or view a selected document.

## Validation

The application performs the following checks during upload:

- File extension validation.
- Empty file validation.
- PDF signature validation.
- Duplicate filename handling.

## Project Status

Currently under development. The PDF upload, validation, listing, and viewing functionalities have been implemented and tested.

## Future Enhancements

- User authentication.
- PDF search functionality.
- PDF summarization using AI.
- Frontend interface for document management.
- Database integration for document metadata.
