from flask import Blueprint, render_template
import asyncio
from celery import current_app as celery_app

main = Blueprint('main', __name__)

@main.route('/')
async def index():
    """
    Renders the main index page.

    This is an asynchronous route that displays the main page of the application.

    Returns:
        A rendered HTML template for the index page.
    """
    return render_template('index.html')

@main.route('/test-celery')
def test_celery():
    """
    Sends a test task to the Celery worker.

    This route is for testing the Celery integration. It sends a predefined
    background task to the Celery worker and returns a confirmation message
    with the task ID.

    Returns:
        str: A string indicating that the task has been sent, including the task ID.
    """
    task = celery_app.send_task('app.tasks.my_background_task', args=[1, 2])
    return f"Task {task.id} sent!"