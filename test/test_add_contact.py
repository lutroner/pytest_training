from pytest_training.model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(name="Name", surname="Surname", phone="+7124124124",
                email="asd@asd.ru", company="PT", address="Moscow"))


def test_add_empty_contact(app):
    app.contact.create(
        Contact(name="", surname="", phone="",
                email="", company="", address=""))
