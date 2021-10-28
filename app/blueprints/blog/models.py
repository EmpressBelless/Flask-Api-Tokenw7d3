from app import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    
    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def to_post(self):
        single_post = {
            'id': self.user_id,
            'content': self.content,
            'title': self.title
    }
        return single_post