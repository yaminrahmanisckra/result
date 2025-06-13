from flask import Flask, render_template
from result_management.models.models import db, Session
from result_management.config import Config


def create_result_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route('/')
    def root_index():
        sessions = Session.query.all()
        return render_template('index.html', sessions=sessions)

    with app.app_context():
        db.create_all()
    return app

