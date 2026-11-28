## Frontend & Backend Integration – Day 11

The NoteBridge frontend is now integrated with the FastAPI backend, providing a simple and user-friendly interface for managing PDF documents.

### Frontend Features

- Clean and responsive user interface.
- Peaceful sage-green and ivory colour theme.
- PDF document upload.
- Display uploaded documents.
- View PDF documents in the browser.
- Delete documents.
- Refresh the document list.

### Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Database:** SQLite
- **Server:** Uvicorn
- **Version Control:** Git and GitHub

### Frontend–Backend Integration

The frontend communicates with the FastAPI backend using JavaScript Fetch API.

| Operation | API Endpoint | Method |
|---|---|---|
| Open application | `/` | GET |
| Upload PDF | `/upload` | POST |
| List PDFs | `/pdfs` | GET |
| View PDF | `/pdfs/{filename}` | GET |
| Delete PDF | `/pdfs/{filename}` | DELETE |
| Retrieve database records | `/documents` | GET |
| Update document | `/documents/{id}` | PUT |
| Delete document and database record | `/documents/{id}` | DELETE |

### Project Structure

```text
NoteBridge/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   └── verify_database.py
│
├── frontend/
│   └── index.html
│
├── uploads/
├── notebridge.db
└── README.md
```

### Running the Application

1. Activate the Python virtual environment.
2. Install the required dependencies.
3. Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

4. Open the application:

```text
http://127.0.0.1:8000/
```

5. Access the API documentation:

```text
http://127.0.0.1:8000/docs
```

### Testing

The following functionalities have been tested:

- PDF uploading and validation.
- File storage.
- SQLite database insertion.
- Document listing.
- PDF viewing.
- Document deletion from both file storage and database.
- Frontend and backend communication.

**Current Status:** Frontend and backend integration completed and tested as part of Phase 1 – Day 11 of the UNAI TECH Virtual Internship Program 2026.