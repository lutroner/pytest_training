from pytest_training.model.group import Group


def test_add_group(app):
    app.group.create(
        Group(name="Бегимоты", header="Живут", footer="В болоте"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
