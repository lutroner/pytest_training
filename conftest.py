import pytest

from pytest_training.fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    yield fixture
