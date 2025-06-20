import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'b7e2f8c1-4e2a-4c7b-9e2d-8f7c2a1b3e4d'
    
    # Database configuration - use SQLite by default for simplicity
    if os.environ.get('DATABASE_URL'):
        # For production with PostgreSQL (Render, Heroku etc.)
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
            SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
    else:
        # For local development and simple deployment - use SQLite
        SQLALCHEMY_DATABASE_URI = 'sqlite:///result.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False






