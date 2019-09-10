import pytest

from simpleapp import create_app, db
import simpleapp.models as model


@pytest.yield_fixture
def app():
    def _app(config_class):
        appl = create_app()
        appl.test_request_context().push()

        db.drop_all()
        from simpleapp.models import Person

        db.create_all()

        return appl

    yield _app
    db.session.remove()
    if str(db.engine.url) == 'SQLALCHEMY_DATABASE_URI':
        db.drop_all()


def test_db_create():
    appl = create_app()
    appl.app_context().push()
    #appl.config.from_mapping(DEBUG=True,
    #                        TESTING=True)
    test_model_to_insert = model.Person(name="Anna", age=12)
    test_model_to_insert.save()
    db.session.commit()

    assert db.session.query(model.Person).one()
