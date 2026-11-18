# NoteBridge

**Connecting students through shared knowledge.**

## About the Project

NoteBridge is a student-focused platform designed to make discovering, sharing and accessing academic learning resources easier.

Students can explore subjects, discover related topics and find learning materials according to their understanding level.

The project is currently under development.

## Key Features (Planned)

- Share and access academic notes.
- Explore related topics within a subject.
- View resource descriptions and concepts covered.
- Identify resource difficulty levels: Beginner, Intermediate and Advanced.
- Search and filter learning resources.
- Discover suitable resources based on learning needs.

## Technology Stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS and JavaScript
- **Database:** SQLite (planned)
- **File Storage:** Local project storage (planned)
- **Server:** Uvicorn
- **Version Control:** Git and GitHub

## Project Architecture

The planned application consists of:

1. **Frontend:** Provides the interface for students.
2. **Backend:** Handles API requests and application logic.
3. **Database:** Stores resource information and metadata.
4. **File Storage:** Stores uploaded learning materials.

## Project Structure

```text
NoteBridge/
├── backend/
│   └── main.py
├── frontend/
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## Current Progress

- [x] Initial project setup
- [x] FastAPI backend setup
- [x] Basic welcome API endpoint
- [x] Git and GitHub setup
- [x] Initial project architecture planning
- [ ] Frontend development
- [ ] Database integration
- [ ] Note upload and management
- [ ] Topic discovery and search
- [ ] Resource descriptions and difficulty levels
- [ ] Note sharing functionality

## How to Run

1. Clone the repository.
2. Activate your Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the backend:

```bash
python -m uvicorn backend.main:app --reload
```

5. Open `http://127.0.0.1:8000` in your browser.

## Project Status

Under Development.
