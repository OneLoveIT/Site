from celery import shared_task
import time

@shared_task
def my_background_task(arg1, arg2):
    """A simple background task."""
    # some long running task
    time.sleep(5)
    return f"Task complete with args: {arg1}, {arg2}"