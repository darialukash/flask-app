import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from simpleapp import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.ConfProd) or app.config.from_object(config.ConfTest)
    # app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev_key'

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
