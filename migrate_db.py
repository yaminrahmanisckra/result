#!/usr/bin/env python3
"""
Database migration script to move from SQLite to PostgreSQL
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Add the result_management directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'result_management'))

from models.models import db, Session, Student, Subject, Mark, CourseRegistration, User
from config import Config

load_dotenv()

def migrate_data():
    """Migrate data from SQLite to PostgreSQL"""
    
    # Create SQLite engine (source)
    sqlite_engine = create_engine('sqlite:///result_management/instance/result.db')
    SQLiteSession = sessionmaker(bind=sqlite_engine)
    sqlite_session = SQLiteSession()
    
    # Create PostgreSQL engine (destination)
    pg_engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    PGSession = sessionmaker(bind=pg_engine)
    pg_session = PGSession()
    
    try:
        print("Starting data migration from SQLite to PostgreSQL...")
        
        # Migrate Sessions
        print("Migrating sessions...")
        sessions = sqlite_session.query(Session).all()
        for session in sessions:
            new_session = Session(
                id=session.id,
                name=session.name,
                term=session.term,
                created_at=session.created_at
            )
            pg_session.add(new_session)
        pg_session.commit()
        print(f"Migrated {len(sessions)} sessions")
        
        # Migrate Students
        print("Migrating students...")
        students = sqlite_session.query(Student).all()
        for student in students:
            new_student = Student(
                id=student.id,
                student_id=student.student_id,
                name=student.name,
                session_id=student.session_id,
                created_at=student.created_at
            )
            pg_session.add(new_student)
        pg_session.commit()
        print(f"Migrated {len(students)} students")
        
        # Migrate Subjects
        print("Migrating subjects...")
        subjects = sqlite_session.query(Subject).all()
        for subject in subjects:
            new_subject = Subject(
                id=subject.id,
                code=subject.code,
                name=subject.name,
                credit=subject.credit,
                subject_type=subject.subject_type,
                dissertation_type=subject.dissertation_type,
                has_retake=subject.has_retake,
                session_id=subject.session_id,
                created_at=subject.created_at
            )
            pg_session.add(new_subject)
        pg_session.commit()
        print(f"Migrated {len(subjects)} subjects")
        
        # Migrate Marks
        print("Migrating marks...")
        marks = sqlite_session.query(Mark).all()
        for mark in marks:
            new_mark = Mark(
                id=mark.id,
                student_id=mark.student_id,
                subject_id=mark.subject_id,
                attendance=mark.attendance,
                continuous_assessment=mark.continuous_assessment,
                part_a=mark.part_a,
                part_b=mark.part_b,
                supervisor_assessment=mark.supervisor_assessment,
                proposal_presentation=mark.proposal_presentation,
                project_report=mark.project_report,
                defense=mark.defense,
                total_marks=mark.total_marks,
                grade_point=mark.grade_point,
                grade_letter=mark.grade_letter,
                is_retake=mark.is_retake,
                created_at=mark.created_at,
                updated_at=mark.updated_at
            )
            pg_session.add(new_mark)
        pg_session.commit()
        print(f"Migrated {len(marks)} marks")
        
        # Migrate Course Registrations
        print("Migrating course registrations...")
        registrations = sqlite_session.query(CourseRegistration).all()
        for reg in registrations:
            new_reg = CourseRegistration(
                id=reg.id,
                student_id=reg.student_id,
                subject_id=reg.subject_id,
                is_retake=reg.is_retake
            )
            pg_session.add(new_reg)
        pg_session.commit()
        print(f"Migrated {len(registrations)} course registrations")
        
        # Migrate Users
        print("Migrating users...")
        users = sqlite_session.query(User).all()
        for user in users:
            new_user = User(
                id=user.id,
                username=user.username,
                email=user.email,
                password_hash=user.password_hash,
                role=user.role,
                created_at=user.created_at
            )
            pg_session.add(new_user)
        pg_session.commit()
        print(f"Migrated {len(users)} users")
        
        print("Data migration completed successfully!")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        pg_session.rollback()
        raise
    finally:
        sqlite_session.close()
        pg_session.close()

if __name__ == '__main__':
    migrate_data() 