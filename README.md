# NoteBridge

**Connecting students through shared knowledge.**

## About the Project

NoteBridge is a student-focused platform designed to make discovering, sharing and accessing academic learning resources easier.

Students can explore subjects, discover related topics and find learning materials according to their understanding level. The platform aims to help students identify relevant resources by understanding what each material covers and how it relates to their learning needs.

The project is currently under development.

## Key Features

- Share and access academic notes and learning materials.
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

NoteBridge follows a simple full-stack architecture consisting of four main components:

1. **Frontend:** Built using HTML, CSS and JavaScript to provide the user interface.
2. **Backend:** Uses Python and FastAPI to handle API requests, validation and application logic.
3. **Database:** SQLite is planned to store resource details, topics and other metadata.
4. **File Storage:** Local storage is planned to maintain uploaded PDF learning materials.

### Communication Flow

Frontend → FastAPI Backend → SQLite Database / PDF File Storage

The frontend sends requests to the backend. The backend processes these requests and interacts with the database or file storage when required.

## Project Structure

```text
NoteBridge/
|-- backend/
|   |-- main.py
|-- frontend/
|-- docs/
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## Project Requirements

### Functional Requirements

- Search for learning materials using subjects and topics.
- Explore related topics.
- View descriptions of study materials.
- Filter resources according to understanding level.
- Access or download available study materials.
- Organize resources according to subjects and topics.

### Non-Functional Requirements

- Simple and user-friendly interface.
- Reasonable search performance.
- Reliable data retrieval.
- Maintainable modular code.
- Compatibility with commonly used web browsers.
- Safe handling of files and user inputs.

### User Requirements

Students should be able to:

- Find relevant study materials easily.
- Understand the contents of a resource before accessing it.
- Select materials according to their knowledge level.
- Access organized learning resources.
- Save time while searching for academic content.

## Project Modules

1. **User Interface Module** – Provides the home page, search interface and resource display.
2. **Search and Topic Module** – Handles topic search, matching results and related topic exploration.
3. **Study Material Management Module** – Organizes materials, descriptions, subjects and topics.
4. **Understanding Level Module** – Categorizes and filters materials based on difficulty.
5. **Material Access Module** – Handles opening and downloading learning resources.
6. **Backend and Database Module** – Processes requests and manages application data.

## Feature Priorities

### Must Have

- Topic and subject search.
- Organized study material listing.
- Material descriptions.
- Basic user interface.
- Access to available learning materials.

### Should Have

- Related topic suggestions.
- Understanding-level filtering.
- Improved search results.
- Handling searches with no matching results.

### Could Have

- Advanced resource recommendations.
- Bookmarks and favorites.
- Personalized learning suggestions.
- Additional search filters.

## Development Roadmap

### Phase 1: Foundation

- [x] Initial project setup.
- [x] FastAPI backend setup.
- [x] Basic welcome API endpoint.
- [x] Git and GitHub setup.
- [x] Initial project architecture planning.
- [x] Requirements identification and module planning.

### Phase 2: Core Development

- [ ] Database structure design.
- [ ] Backend API development.
- [ ] Frontend development.
- [ ] Topic search functionality.
- [ ] Study material listing.
- [ ] Resource descriptions.
- [ ] Material access and downloading.

### Phase 3: Additional Features

- [ ] Related topic discovery.
- [ ] Understanding-level filtering.
- [ ] Improved search functionality.
- [ ] Resource organization and management.

### Phase 4: Testing and Improvements

- [ ] Test individual modules.
- [ ] Test frontend and backend integration.
- [ ] Handle invalid inputs and missing files.
- [ ] Fix bugs and improve usability.

## Development Approach

NoteBridge will be developed using a modular approach. Each module will be implemented and tested independently before integrating it into the complete application.

Development will prioritize essential features first, followed by improvements based on available time and project requirements.

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

**Under Development**

The initial backend setup and project planning are completed. Database integration, frontend development, search functionality and study material management are planned for the upcoming development stages.