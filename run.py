"""
This script runs the Flask application.

It creates an instance of the app and then runs it.
The Flask configuration can be set using the FLASK_CONFIG environment variable.
"""
import os
from app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")

if __name__ == "__main__":
    app.run()