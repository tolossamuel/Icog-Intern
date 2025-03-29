# HR-FQA: AI-Powered FAQ System

## Overview

HR-FQA is an AI-powered FAQ system that answers questions based on domain knowledge. We use **meta-programming** techniques to store **Icog HR activity knowledge** in a **graph format** for efficient knowledge representation.

## Features

* **Domain-Specific Knowledge** : Answers are based on predefined HR-related knowledge.
* **Graph-Based Knowledge Representation** : Uses meta-programming to store HR activities efficiently.
* **FastAPI Backend** : Built using FastAPI for high-performance API responses.
* **Dockerized Deployment** : Runs in a containerized environment for easy deployment.
* **CORS Handling** : Allows access from different domains for seamless integration.

## Installation

### Prerequisites

* Python 3.8+
* FastAPI
* Docker

### Clone the Repository

```bash
 git clone https://github.com/tolossamuel/hr-fqa.git
 cd hr-fqa
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
uvicorn app:FastAPI --host 0.0.0.0 --port 8000 --reload
```

## Deployment

### Using Docker

```bash
docker build -t hr-fqa .
docker run -d -p 8000:8000 hr-fqa
```

### Push to Docker Hub

```bash
docker tag hr-fqa samueltolossa/hr-fqa:latest
docker push samueltolossa/hr-fqa:latest
```

### Deploy on GitHub Pages (For Frontend)

1. Push your static files (HTML, CSS, JavaScript) to a GitHub repository.
2. Go to `Settings > Pages` in your repository.
3. Select the `main` branch as the source.
4. Your site will be available at `https://tolossamuel.github.io/hr-fqa/`.

## API Endpoints

### Ask a Question

**GET** `/ask-her/?question=your-question-here`

Example:

```bash
curl -X GET "https://hr-fqa-latest.onrender.com/ask-her/?question=what%20is%20mentoring"
```

### CORS Configuration (For External Access)

To enable CORS, modify `main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Added new feature"`
4. Push to branch: `git push origin feature-name`
5. Open a pull request.
