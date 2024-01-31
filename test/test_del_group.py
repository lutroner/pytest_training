from pytest_training.model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="Test", footer="Test"))
    app.group.delete_first_group()
