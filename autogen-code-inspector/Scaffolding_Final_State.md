autogen-code-inspector/
│
├── docker-compose.yml         # Defines all services and networks
├── .env                       # Environment variables
│
├── orchestrator/              # Runs AutoGen agents
│   ├── Dockerfile
│   └── main.py
│
├── trainer/                   # Fine-tunes and serves the LLM
│   ├── Dockerfile
│   ├── train.py
│   ├── serve.py
│   ├── model/
│   └── data/
│
├── vectordb/                  # Vector database container (e.g., Chroma or FAISS)
│   ├── Dockerfile
│   └── app.py
│
├── indexer/                   # Indexes codebase and SQL schema
│   ├── Dockerfile
│   ├── index.py
│   └── codebase/              # Contains .cs, .vb, .sql files
│
├── ollama/                    # Your custom Ollama container with Mistral
│   ├── Dockerfile
│   └── ollama_start.sh        # Starts Ollama and preloads models
│
├── frontend/                  # React-based frontend for file uploads
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── FileUpload.jsx  # File upload component
│   │   └── App.jsx             # Main React app
│   ├── package.json            # NPM dependencies
│   └── .env                    # Environment variables for the frontend
│
├── backend/                   # Flask backend for file processing and interaction
│   ├── app.py                  # Main Flask app
│   ├── decompiler.py           # Handles DLL decompiling logic
│   ├── sql_parser.py           # Handles SQL script processing
│   ├── file_upload.py          # Handles ZIP file uploads and extraction
│   ├── metadata/               # Optional folder for additional metadata
│   │   ├── info.txt            # Additional information about the file or process
│   │   └── version.txt         # Versioning information for the files
│   └── celery/                 # Celery configuration and task management
│       ├── celery.py           # Celery configuration (message broker, etc.)
│       └── tasks.py            # Celery tasks for file processing (decompiling DLLs, parsing DACPACs, etc.)
│
├── celery-worker/              # Celery worker container for asynchronous task processing
│   ├── Dockerfile              # Container image for running Celery workers
│   └── celery_start.sh         # Script to start Celery worker
│
├── redis/                      # Redis container for Celery broker
│   └── Dockerfile              # Redis container image
│
└── flower/                     # Flower container for monitoring Celery tasks
    ├── Dockerfile              # Flower container image
    └── flower_start.sh         # Script to start Flower for monitoring Celery tasks
