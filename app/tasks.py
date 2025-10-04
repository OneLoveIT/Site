from celery import shared_task
import time

@shared_task
def my_background_task(arg1, arg2):
    """
    A simple background task that simulates a long-running operation.

    This task takes two arguments, waits for a few seconds, and then returns
    a string indicating that the task is complete.

    Args:
        arg1: The first argument for the task.
        arg2: The second argument for the task.

    Returns:
        str: A string confirming the task's completion and its arguments.
    """
    # some long running task
    time.sleep(5)
    return f"Task complete with args: {arg1}, {arg2}"