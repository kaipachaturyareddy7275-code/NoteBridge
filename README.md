## Current Progress

### Completed

- Initial project and backend setup
- FastAPI application configuration
- PDF upload API (`POST /upload`)
- Uploaded PDF listing API (`GET /pdfs`)
- PDF viewing API (`GET /pdfs/{filename}`)
- PDF deletion API (`DELETE /pdfs/{filename}`)
- Filename and file type validation
- Empty file and invalid PDF validation
- Duplicate filename handling
- PDF deletion error handling
- SQLite database integration
- Document record creation and retrieval
- Document update and deletion using database IDs
- Synchronization of PDF filenames and file paths during updates
- Deletion of both PDF files and their database records
- API documentation using Swagger UI
- API testing using Swagger UI
- GitHub version control and project updates

### In Progress

- Improving backend functionality
- Frontend development

### Planned

- Student-friendly interface
- Note sharing functionality
- Additional testing and validation
- Integration of frontend with backend
- AI-powered document question-answering functionality

---

## Day 10 Implementation

### Backend Development and API Integration

The backend was improved to connect PDF file operations with database records.

### Document Management APIs

**1. GET `/documents`**

- Retrieves all document records stored in the database.
- Returns document details and the total number of records.

**2. PUT `/documents/{document_id}`**

- Updates a document using its database ID.
- Validates the new PDF filename.
- Renames the actual PDF file.
- Updates both the filename and file path in the database.
- Handles missing documents and duplicate filenames.

**3. DELETE `/documents/{document_id}`**

- Finds the document using its database ID.
- Deletes the corresponding PDF file if it exists.
- Removes the document record from the database.
- Handles requests for non-existing document IDs.

### Testing Results

The following operations were tested using Swagger UI:

- Successfully uploaded a PDF and stored its details in SQLite.
- Retrieved document information using the GET API.
- Renamed a PDF using the PUT API.
- Verified that both the physical filename and database file path were updated.
- Deleted a PDF using the document ID.
- Verified that the corresponding database record was removed.
- Verified that the deleted PDF was no longer present in the uploaded PDF list.
- Tested invalid file uploads and received appropriate 400 error responses.
- Tested deletion of a non-existing document and received a 404 error response.

All the above tested operations returned the expected results.

### API Endpoints

| Method | Endpoint                   | Purpose                              |
| ------ | -------------------------- | ------------------------------------ |
| GET    | `/`                        | Welcome message                      |
| POST   | `/upload`                  | Upload a PDF                         |
| GET    | `/pdfs`                    | List uploaded PDFs                   |
| GET    | `/pdfs/{filename}`         | View a PDF                           |
| DELETE | `/pdfs/{filename}`         | Delete a PDF by filename             |
| GET    | `/documents`               | Retrieve database records            |
| PUT    | `/documents/{document_id}` | Rename a PDF and update its record   |
| DELETE | `/documents/{document_id}` | Delete a PDF and its database record |

### Tools and Technologies Used

- Python
- FastAPI
- SQLite
- SQL
- Swagger UI
- Git and GitHub

---

## Future Improvements

- Develop a student-friendly frontend.
- Integrate the frontend with the existing backend APIs.
- Implement note-sharing functionality.
- Store user questions and AI-generated answers.
- Implement relationships between documents, questions, and answers.
- Explore AI-based document question-answering features.
