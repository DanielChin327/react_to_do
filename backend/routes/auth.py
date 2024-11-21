# routes/auth.py

from flask import Blueprint, request, jsonify  # Flask utilities
from flask_bcrypt import Bcrypt  # For password hashing
from flask_jwt_extended import create_access_token  # JWT for authentication
import mysql.connector
from config import DB_CONFIG  # Database configuration

bcrypt = Bcrypt()  # Initialize bcrypt for password hashing
auth_blueprint = Blueprint('auth', __name__)  # Create a blueprint for authentication routes

# Function to establish a database connection
def get_connection():
    """
    Create and return a connection object for the MySQL database.
    """
    return mysql.connector.connect(**DB_CONFIG)

# Route to register a new user
@auth_blueprint.route('/register', methods=['POST'])
def register_user():
    """
    API endpoint to register a new user.
    Request JSON body:
      - username: The username of the new user.
      - password: The password of the new user (hashed before saving).
    Response:
      - Message confirming registration.
    """
    data = request.json  # Get JSON data from the request body
    username = data.get('username')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')  # Hash the password

    conn = get_connection()  # Establish database connection
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"  # SQL query to insert user
    cursor.execute(query, (username, password))  # Execute query with provided data
    conn.commit()  # Commit the transaction to save changes
    conn.close()  # Close the database connection
    return jsonify({'message': 'User registered successfully'})  # Return success response

# Route to log in a user
@auth_blueprint.route('/login', methods=['POST'])
def login_user():
    """
    API endpoint to authenticate a user and issue a JWT token.
    Request JSON body:
      - username: The username of the user.
      - password: The password of the user (verified against the hashed password in the database).
    Response:
      - A JWT token if authentication is successful.
      - Error message if authentication fails.
    """
    data = request.json  # Get JSON data from the request body
    username = data.get('username')
    password = data.get('password')

    conn = get_connection()  # Establish database connection
    cursor = conn.cursor(dictionary=True)  # Use dictionary format for easier key-value access
    query = "SELECT * FROM users WHERE username = %s"  # SQL query to find the user
    cursor.execute(query, (username,))
    user = cursor.fetchone()  # Fetch the user record
    conn.close()  # Close the database connection

    # Check if user exists and password matches
    if user and bcrypt.check_password_hash(user['password'], password):
        token = create_access_token(identity=user['id'])  # Generate a JWT token for the user
        return jsonify({'token': token, 'message': 'Login successful'})  # Return the token and success message
    else:
        return jsonify({'message': 'Invalid credentials'}), 401  # Return error if authentication fails
