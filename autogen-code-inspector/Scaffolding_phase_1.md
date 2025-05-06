autogen-code-inspector/
│
├── docker-compose.yml         # Defines all services and networks
├── .env                       # Environment variables
│
├── orchestrator/              # Runs AutoGen agents
│   ├── Dockerfile
│   └── main.py
│
├── frontend/                  # React-based frontend for file uploads
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── FileUpload.jsx  # Simple file upload component
│   │   └── App.jsx             # Main React app
│   ├── package.json            # NPM dependencies
│   └── .env                    # Environment variables for the frontend
│
├── backend/                   # Flask backend for file processing and interaction
│   ├── app.py                  # Main Flask app
│   ├── file_upload.py          # Handles ZIP file uploads and extraction
│   └── celery/
│       ├── celery.py           # Celery configuration (message broker, etc.)
│       └── tasks.py            # Celery tasks for background processing
│
├── celery-worker/              # Celery worker container for asynchronous task processing
│   ├── Dockerfile              # Container image for running Celery workers
│   └── celery_start.sh         # Script to start Celery worker
│
└── redis/                      # Redis container for Celery broker
    └── Dockerfile              # Redis container image

# Incremental Development Plan

## 1. Initial Setup: Basic Environment
### Step 1: Set up the basic Docker environment and project scaffolding.
- **docker-compose.yml**: Define the basic Docker services, networks, and environment variables.
- **Backend**: Set up a minimal Flask backend (`app.py`) to handle basic API requests and testing.
- **Frontend**: Create a minimal React app with basic file upload functionality.
  
**Goal**: Ensure that the backend and frontend can communicate, and file uploads work correctly.

## 2. Celery Integration (Async Task Handling)
### Step 2: Integrate Celery for task management.
- Add a basic **Celery worker** container (`celery-worker/`) to the `docker-compose.yml`.
- Create a simple **Celery task** in `tasks.py` (for example, a task that simulates processing a file upload).
- Integrate **Redis** as a message broker for Celery in the `docker-compose.yml`.
- Modify the backend to send file processing requests to Celery for background task execution.

**Goal**: Ensure Celery can handle simple asynchronous tasks.

## 3. File Upload Handling (ZIP Files)
### Step 3: Implement logic to upload ZIP files containing code and schema.
- Create a file upload endpoint in the backend (`file_upload.py`) that accepts ZIP files.
- Extract ZIP files and store them temporarily in a specific directory.

**Goal**: Make sure that ZIP files are correctly uploaded and extracted.

## 4. Basic Code and Schema Parsing
### Step 4: Add basic DLL decompiling and DACPAC parsing functionality.
- Implement simple **DLL decompiling** logic in `decompiler.py` (you can use a Python library like `pycil` or `unpy2exe`).
- Implement basic **DACAPC parsing** logic in `sql_parser.py`.

**Goal**: Ensure that the backend can process both code (DLL) and SQL schema (DACPAC).

## 5. Celery Task for Parsing
### Step 5: Move the parsing logic into Celery tasks.
- Use Celery to run decompiling and parsing as background tasks when a ZIP file is uploaded.

**Goal**: Ensure that tasks are properly queued and executed asynchronously by Celery.

## 6. Frontend Feedback and Task Monitoring
### Step 6: Provide feedback on task status in the frontend.
- Implement a basic **progress bar** or **task status indicator** on the frontend.
- Use Celery **task status** to show progress or completion of background tasks.

**Goal**: Enable users to monitor the progress of background tasks (like file parsing).

## 7. Vector Database Integration (Basic Version)
### Step 7: Integrate the vector database (e.g., Chroma or FAISS).
- Set up a basic **vector database container** (`vectordb/`) in Docker.
- Implement the functionality to store the parsed code and SQL schema in the vector database.
- Ensure the backend can query the vector DB and retrieve relevant information.

**Goal**: Store parsed data in a vector format and provide basic search/query functionality.

## 8. Ollama Integration for LLM Tasks
### Step 8: Integrate Ollama for LLM-based tasks (e.g., code analysis, summarization).
- Ensure that the **Ollama container** is set up and running (`ollama/`).
- Modify the backend to call Ollama for specific tasks like code summarization or documentation generation.

**Goal**: Test the integration between your backend and the Ollama container.

## 9. Final Touches: Monitoring and UI Enhancements
### Step 9: Integrate Flower to monitor Celery tasks.
- Add a **Flower** container for real-time task monitoring.
- Optionally, enhance the frontend to show task progress with Flower’s live updates.

**Goal**: Improve user experience with live task tracking.

## 10. Testing and CI/CD Integration
### Step 10: Write tests for all services.
- Add unit tests for the backend logic and Celery tasks.
- Set up **CI/CD pipelines** for automated testing and deployment.

**Goal**: Ensure that the system is well-tested and deployable.
