from pytest_training.model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Test"))
    app.contact.modify(Contact(name="Modified"))


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(phone="+12345678"))
    app.contact.modify(Contact(phone="Modified"))
