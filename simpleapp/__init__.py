from flask import Flask, request, escape
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from simpleapp.config import ConfProd, ConfDev

db = SQLAlchemy()
migrate = Migrate()


def create_app(configure=ConfDev):
    app = Flask(__name__)
    app.config.from_object(configure)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!'
        #return 'Hello World!'

    from . import models
    from .models import Person

    with app.app_context() as context:
        context.push()
        db.create_all()

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'Person': Person}

    return app
