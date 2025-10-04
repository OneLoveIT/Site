from celery import Celery

def init_celery(app):
    """
    Initializes and configures a Celery instance for a Flask application.

    This function creates a Celery instance, configures it using the settings
    from the Flask application, and sets up a custom task class that ensures
    tasks are run within the Flask application context.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        Celery: The configured Celery instance.
    """
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        """
        A Celery Task that runs within a Flask application context.

        This custom task class ensures that when a Celery task is executed,
        it has access to the Flask application context, which is necessary
        for tasks that need to interact with Flask extensions or application-
        specific configurations.
        """
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery