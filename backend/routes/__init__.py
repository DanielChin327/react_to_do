from routes.auth import auth_blueprint
from routes.task import task_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(task_blueprint, url_prefix='/tasks')
