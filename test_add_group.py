import pytest

from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture


def test_add_group(self, app):
    self.app.login(username="admin", password="secret")
    self.app.create_group(
        Group(name="Бегимоты", header="Живут", footer="В болоте"))
    self.app.logout()


def test_add_empty_group(self, app):
    self.app.login(username="admin", password="secret")
    self.app.create_group(Group(name="", header="", footer=""))
    self.app.logout()
