from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import register_blueprints

# Import the db instance from models
from models import db

# Create the Flask app
app = Flask(__name__)

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/react_to_do'  # Update your DB credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)  # Initialize the db with the app
migrate = Migrate(app, db)  # Initialize migrations
CORS(app)  # Enable CORS

# Register blueprints for routes
register_blueprints(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
