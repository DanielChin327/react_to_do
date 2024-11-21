# app.py

from flask import Flask
from flask_cors import CORS
from routes.tasks import tasks_blueprint  # Blueprint for task-related routes
from routes.auth import auth_blueprint    # Blueprint for authentication-related routes

# Create a Flask application instance
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) to allow frontend requests
CORS(app)

# Register the task management routes under the `/tasks` URL prefix
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

# Register the authentication routes under the `/auth` URL prefix
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Start the application if this script is run directly
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development (auto-reload on changes)
