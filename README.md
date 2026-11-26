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
- API documentation using Swagger UI
- Basic API testing using Swagger UI
- Testing of PDF upload, listing, viewing, and deletion functionalities

### In Progress
- Improving backend functionality
- Database integration
- Frontend development

### Planned
- Student-friendly interface
- Note sharing functionality
- Additional testing and validation
- Integration of frontend with backend

## Day 8 Implementation

### PDF Resource Management

A PDF deletion feature was added to the existing FastAPI backend.

**New API Endpoint:**
- `DELETE /pdfs/{filename}` – Deletes an uploaded PDF using its filename.

**Functionality:**
- Validates the PDF filename.
- Checks whether the requested PDF exists.
- Deletes the selected PDF.
- Returns a success message after deletion.
- Handles missing PDF files with an appropriate error response.

### Testing Results
- Successfully deleted an existing PDF.
- Verified that the deleted PDF was no longer listed.
- Tested deletion of a non-existing PDF and received a 404 error.
- Verified that existing upload, listing, and viewing functionalities continued working.

## Database Integration

NoteBridge uses SQLite to store information about uploaded PDF documents.

### Database Details
- Database: SQLite
- Database file: `notebridge.db`
- Python library: `sqlite3`

### Documents Table

The Documents table stores:
- Document ID
- PDF filename
- File path
- Upload date

### Database Operations

The application currently supports:

- **Create:** Insert uploaded PDF details into the database.
- **Read:** Retrieve stored document details.
- **Update:** Modify document information.
- **Delete:** Remove document records.

### Database Connection

The application connects to SQLite using Python's built-in `sqlite3` module.

The database connection and table creation logic are maintained in `backend/database.py`.

### Future Improvements

- Store user questions in the database.
- Store AI-generated answers.
- Implement relationships between documents, questions and answers.
