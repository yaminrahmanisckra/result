from setuptools import setup, find_packages

setup(
    name="result_management",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'reportlab',
        'openpyxl',
        'werkzeug'
    ],
) 