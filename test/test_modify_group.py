from pytest_training.model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="Test", footer="Test"))
    app.group.modify(Group(name="New Group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="Test", footer="Test"))
    app.group.modify(Group(header="New Header"))
