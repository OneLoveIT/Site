"""
This script initializes the Celery worker for the Flask application.

It creates a Flask application instance, initializes Celery with the application's
configuration, and imports the tasks so they are registered with the worker.
To run the Celery worker, you would typically use a command like:
`celery -A celery_worker.celery worker --loglevel=info`
"""
from app import create_app
from app.celery_utils import init_celery
import os

app = create_app(os.getenv("FLASK_CONFIG") or "default")
celery = init_celery(app)

# Import your tasks here
import app.tasks