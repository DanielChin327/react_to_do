# app.py
from flask import Flask
from flask_cors import CORS
from routes.tasks import tasks_blueprint
from routes.auth import auth_blueprint

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Register Blueprints
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)
