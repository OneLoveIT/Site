from flask import Flask
from .routes import main
import asyncio

def create_app(config_name):
    """
    Creates and configures a Flask application.

    This function initializes a Flask application, sets up its configuration,
    initializes Celery, and registers the main blueprint.

    Args:
        config_name (str): The name of the configuration to use for the app.
                           This is not currently used but is a placeholder for
                           future configuration management.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    # A simple default config
    app.config.from_mapping(
        SECRET_KEY='dev',
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    )

    # Make Flask app use asyncio
    app.config['ASYNC_MODE'] = True

    from .celery_utils import init_celery
    init_celery(app)

    app.register_blueprint(main)

    return app