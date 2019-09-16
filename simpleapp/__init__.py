from flask import request
from flask_api import FlaskAPI
from flask_api.decorators import set_parsers
from flask_api.parsers import JSONParser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from simpleapp.config import ConfProd, ConfDev


db = SQLAlchemy()
migrate = Migrate()


def create_app(configure=ConfProd):
    app = FlaskAPI(__name__)
    app.config.from_object(configure)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return 'Hello World!'

    from . import models
    from .models import Person

    with app.app_context() as context:
        context.push()
        db.create_all()

        @app.route('/database', methods=['GET', 'POST'])
        @set_parsers(JSONParser)
        def examlpe():

            if request.method == "GET":
                content = {'Persons in DB': len(db.session.query(Person).all())}
                return content
            elif request.method == "POST":
                try:
                    content = request.data
                    name = content['name']
                    age = content['age']
                    newPerson = Person(name, age)
                    newPerson.save()
                    db.session.commit()
                    print(db.session.query(Person)[-1])
                    return content

                except KeyError:
                    return content

    return app
