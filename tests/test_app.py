import pytest
import os

from simpleapp import create_app, db
from simpleapp.config import ConfTest, ConfDev
import simpleapp.models as model


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(ConfTest)
    return app


def test_test_conf(app):
    app.config.from_object(ConfTest)
    assert app.config['DEBUG']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_TEST_URL')
    assert app.config['TESTING']
    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']


# def test_dev_conf(app):
#    app.config.from_object(ConfDev)
#    assert app.config['DEBUG']
#    assert app.config['SQLALCHEMY_DATABASE_URI'] #== os.environ.get('DATABASE_DEV_URL')
#    assert app.config['TESTING']
#    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']

def test_index(app):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data


def test_db(app):
    with app.app_context() as context:
        context.push()
        db.drop_all()
        db.create_all()

        from simpleapp.models import Person

        test_person = Person(name="Anna", age=12)
        test_person.save()
        db.session.commit()

    assert db.session.query(Person).one()
