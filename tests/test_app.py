import pytest

# from test.support.configure_test import app
from simpleapp import *
import simpleapp.models as model


def test_db_create():
    app = create_app()
    app.config.from_mapping(DEBUG=True,
                            TESTING=True)
    db.drop_all()
    test_model_to_insert = model.Person(
        cool_field="test name", cooler_field="Cooler String"
    )
    test_model_to_insert.save()
    db.session.commit()

    assert db.session.query(model.Person).one()
