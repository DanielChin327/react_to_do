# models/tasks.py

import mysql.connector  # MySQL connector for Python
from config import DB_CONFIG  # Import database configuration

# Function to establish a connection to the MySQL database
def get_connection():
    """
    Create and return a connection object for the MySQL database.
    """
    return mysql.connector.connect(**DB_CONFIG)

# Function to fetch all tasks for a specific user
def fetch_all_tasks(user_id):
    """
    Retrieve all tasks associated with a given user from the database.
    :param user_id: The ID of the user whose tasks need to be fetched.
    :return: A list of task dictionaries.
    """
    conn = get_connection()  # Establish database connection
    cursor = conn.cursor(dictionary=True)  # Use dictionary format for easier key-value access
    query = "SELECT * FROM tasks WHERE user_id = %s"  # SQL query to get tasks for the user
    cursor.execute(query, (user_id,))  # Execute query with the user_id as a parameter
    tasks = cursor.fetchall()  # Fetch all matching records
    conn.close()  # Close the database connection
    return tasks  # Return the list of tasks

# Function to add a new task to the database
def add_task(user_id, title, description, priority, due_date):
    """
    Insert a new task into the database for a specific user.
    :param user_id: The ID of the user adding the task.
    :param title: Title of the task.
    :param description: Description of the task.
    :param priority: Priority level of the task.
    :param due_date: Due date of the task.
    :return: The ID of the newly created task.
    """
    conn = get_connection()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor for executing queries
    query = """
        INSERT INTO tasks (user_id, title, description, priority, due_date, completed)
        VALUES (%s, %s, %s, %s, %s, %s)
    """  # SQL query to insert a new task
    cursor.execute(query, (user_id, title, description, priority, due_date, False))  # Execute query with provided data
    conn.commit()  # Commit the transaction to save changes
    task_id = cursor.lastrowid  # Get the ID of the newly inserted task
    conn.close()  # Close the database connection
    return task_id  # Return the new task ID
