import pytest

from pytest_training.fixture.application import Application
from pytest_training.model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    yield fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(
        Group(name="Бегимоты", header="Живут", footer="В болоте"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
