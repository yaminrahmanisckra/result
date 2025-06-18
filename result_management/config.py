import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'b7e2f8c1-4e2a-4c7b-9e2d-8f7c2a1b3e4d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///result.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False






