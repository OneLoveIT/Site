# Flask and Celery Boilerplate

This repository provides a boilerplate for building web applications using Flask and Celery. It's designed to be a starting point for projects that require a web front-end and asynchronous background task processing.

## Features

- **Flask:** A lightweight and flexible web framework for Python.
- **Celery:** A powerful distributed task queue for handling background jobs.
- **Redis:** Used as the message broker and result backend for Celery.
- **Async Support:** The Flask application is configured to support asynchronous routes.
- **Modular Structure:** The application is organized into blueprints for better code management.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7+
- Redis

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure Redis is running:**
    Make sure you have a Redis server running on its default port (6379).

## Running the Application

You need to run two processes in separate terminals: the Flask web server and the Celery worker.

1.  **Run the Flask Web Server:**
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

2.  **Run the Celery Worker:**
    In a new terminal, run the following command from the project's root directory:
    ```bash
    celery -A celery_worker.celery worker --loglevel=info
    ```

## Usage

- **`GET /`**: This is the main page of the application, which simply displays a welcome message.
- **`GET /test-celery`**: This endpoint sends a sample background task to the Celery worker. When you access this URL, a task is queued, and the page will display the task ID. The Celery worker will then execute the task, which involves a 5-second delay to simulate a long-running process.

## Project Structure

```
.
├── app/                  # Main application package
│   ├── static/           # Static files (CSS, JS)
│   ├── templates/        # HTML templates
│   ├── __init__.py       # Application factory
│   ├── celery_utils.py   # Celery setup utility
│   ├── routes.py         # Application routes
│   └── tasks.py          # Celery tasks
├── celery_worker.py      # Celery worker entry point
├── requirements.txt      # Python dependencies
├── run.py                # Script to run the Flask app
└── README.md             # This file
```