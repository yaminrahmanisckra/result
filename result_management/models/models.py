from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    term = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    students = db.relationship('Student', backref='session', lazy=True)
    subjects = db.relationship('Subject', backref='session', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    marks = db.relationship('Mark', backref='student', lazy=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Float, nullable=False)
    subject_type = db.Column(db.String(20), nullable=False)  # Theory/Dissertation
    dissertation_type = db.Column(db.String(20), nullable=True)  # For dissertation subjects
    has_retake = db.Column(db.Boolean, default=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    marks = db.relationship('Mark', backref='subject', lazy=True)

class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    
    # Theory marks
    attendance = db.Column(db.Float, nullable=True)
    continuous_assessment = db.Column(db.Float, nullable=True)
    part_a = db.Column(db.Float, nullable=True)
    part_b = db.Column(db.Float, nullable=True)
    
    # Dissertation marks
    supervisor_assessment = db.Column(db.Float, nullable=True)
    proposal_presentation = db.Column(db.Float, nullable=True)
    project_report = db.Column(db.Float, nullable=True)
    defense = db.Column(db.Float, nullable=True)
    
    total_marks = db.Column(db.Float, nullable=False)
    grade_point = db.Column(db.Float, nullable=False)
    grade_letter = db.Column(db.String(2), nullable=False)
    is_retake = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CourseRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    is_retake = db.Column(db.Boolean, default=False)
    __table_args__ = (db.UniqueConstraint('student_id', 'subject_id', 'is_retake', name='_student_subject_retake_uc'),)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
