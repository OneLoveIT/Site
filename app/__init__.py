from flask import Flask
from .routes import main
import asyncio

def create_app(config_name):
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