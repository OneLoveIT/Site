from app import create_app
from app.celery_utils import init_celery
import os

app = create_app(os.getenv("FLASK_CONFIG") or "default")
celery = init_celery(app)

# Import your tasks here
import app.tasks