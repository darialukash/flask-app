import pytest
import os

from simpleapp import create_app, db
import simpleapp.models as model

POSTGRES_USER = os.environ.get("TESTING_POSTGRES_USER")
POSTGRES_PW = os.environ.get("TESTING_POSTGRES_PW")
POSTGRES_URL = os.environ.get("TESTING_POSTGRES_URL")
POSTGRES_DB = os.environ.get("TESTING_POSTGRES_DB")


def create_db_url(user, pw, url, db):
    return f"postgresql://{user}:{pw}@{url}/{db}"


DATABASE_TEST_URL = create_db_url(POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB)


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_TEST_URL') or \
                                            'postgresql://postgres:postgres@localhost/flaskdb'
    app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
    return app


def test_index(app):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data


def test_db(app):
    with app.test_request_context() as context:
        context.push()
        db.drop_all()
        db.create_all()

        from simpleapp.models import Person

        test_person = Person(name="Anna", age=12)
        test_person.save()
        db.session.commit()

    assert db.session.query(Person).one()
