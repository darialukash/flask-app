from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from simpleapp.config import ConfProd

db = SQLAlchemy()
migrate = Migrate()


def create_app(configure=ConfProd):
    app = Flask(__name__)
    app.config.from_object(configure)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return 'Hello World!'

    from . import models

    with app.app_context() as context:
        context.push()
        db.create_all()

    return app
