import pytest


@pytest.fixture(autouse=True, scope='module')
def enable_test_mode():
    from example.app import app
    app.testing = True


@pytest.fixture
def client():
    from example.app import app
    with app.test_client() as c:
        yield c
