# routes/tasks.py

from flask import Blueprint, request, jsonify  # Flask utilities for handling requests and responses
from models.tasks import fetch_all_tasks, add_task  # Import task-related database functions

# Create a blueprint for task-related routes
tasks_blueprint = Blueprint('tasks', __name__)

# Route to fetch all tasks for a user
@tasks_blueprint.route('/', methods=['GET'])
def get_tasks():
    """
    API endpoint to retrieve all tasks for a specific user.
    Query parameter:
      - user_id: The ID of the user.
    Response:
      - List of task objects in JSON format.
    """
    user_id = request.args.get('user_id')  # Get user ID from query parameters
    tasks = fetch_all_tasks(user_id)  # Fetch tasks from the database
    return jsonify(tasks)  # Return the tasks as a JSON response

# Route to create a new task
@tasks_blueprint.route('/', methods=['POST'])
def create_task():
    """
    API endpoint to add a new task to the database.
    Request JSON body:
      - user_id: The ID of the user adding the task.
      - title: Title of the task.
      - description: Description of the task.
      - priority: Priority level of the task.
      - due_date: Due date of the task.
    Response:
      - Message and ID of the newly created task.
    """
    data = request.json  # Get JSON data from the request body
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority')
    due_date = data.get('due_date')

    # Call the function to add the task to the database
    task_id = add_task(user_id, title, description, priority, due_date)
    return jsonify({'task_id': task_id, 'message': 'Task added successfully'})  # Return success response
