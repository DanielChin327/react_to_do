from models import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(75), nullable=False)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username
        }
