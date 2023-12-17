from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from app import db

# db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # New field to indicate admin status

    red_flags = db.relationship('RedFlag', backref='user', lazy=True)
    interventions = db.relationship('Intervention', backref='user', lazy=True)


class RedFlag(db.Model):
    __tablename__ = 'redflag'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(20), default='pending')
    image_file = db.Column(db.String, nullable=False)
    video_file = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'investigating', 'rejected', 'resolved'
    category = db.Column(db.String(255), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Intervention(db.Model):
    __tablename__ = 'intervention'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(20), default='pending')
    image_file = db.Column(db.String, nullable=False)
    video_file = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'investigating', 'rejected', 'resolved'
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class AdminAction(db.Model):
    __tablename__ = 'adminAction'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    post_type = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
