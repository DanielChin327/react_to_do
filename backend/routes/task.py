from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.task import Task
from models import db

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks])

@task_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.json
    new_task = Task(
        user_id=user_id,
        title=data.get('title'),
        description=data.get('description'),
        priority=data.get('priority'),
        due_date=data.get('due_date'),
        completed=False
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully', 'task': new_task.to_dict()})
