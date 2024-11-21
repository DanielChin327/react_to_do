from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import register_blueprints

# Initialize Flask app
app = Flask(__name__)

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/react_to_do'  # Update with your DB user/password
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids SQLAlchemy warning

# Initialize extensions
db = SQLAlchemy(app)  # ORM for database
migrate = Migrate(app, db)  # Migration tool for schema changes
CORS(app)  # Enable Cross-Origin Resource Sharing

# Import and register models
from models import user, task  # Ensure these modules define the User and Task models

# Register blueprints for routes
register_blueprints(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
