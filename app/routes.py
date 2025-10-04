from flask import Blueprint, render_template
import asyncio
from celery import current_app as celery_app

main = Blueprint('main', __name__)

@main.route('/')
async def index():
    return render_template('index.html')

@main.route('/test-celery')
def test_celery():
    task = celery_app.send_task('app.tasks.my_background_task', args=[1, 2])
    return f"Task {task.id} sent!"