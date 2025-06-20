#!/usr/bin/env python3
"""
Setup script for PostgreSQL database
"""

import os
import sys
from dotenv import load_dotenv

# Add the result_management directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'result_management'))

from app import create_app
from models.models import db

load_dotenv()

def setup_database():
    """Create all database tables"""
    
    app = create_app()
    
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    setup_database() 