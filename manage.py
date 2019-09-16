import pytest
from flask_script import Manager
from simpleapp import create_app

manager = Manager(create_app)


@manager.command
def test():
    """Runs the tests."""
    pytest.main(["-s", "tests"])


if __name__ == "__main__":
    manager.run()
