from datetime import datetime
from init import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Contact(db.Model):
    name= db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}', '{self.message}')"

class Contact2(db.Model):
    name= db.Column(db.String(20), nullable=True, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    project_choice = db.Column(db.Integer, nullable=False)
    Agree= db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"Contact2('{self.name}', '{self.email}', '{self.project_choice}',{self.Agree})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
