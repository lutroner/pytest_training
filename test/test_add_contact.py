from selenium import webdriver
from selenium.webdriver.common.by import By

from contact import Contact


class TestAddGroup:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 600)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_contact_page()
        self.create_contact(
            Contact(name="Name", surname="Surname", phone="+7124124124",
                    email="asd@asd.ru", company="PT", address="Moscow"))
        self.open_contact_page()
        self.logout()

    def test_add_empty_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_contact_page()
        self.create_contact(
            Contact(name="", surname="", phone="",
                    email="", company="", address=""))
        self.open_contact_page()
        self.logout()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def create_contact(self, contact):
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.name)
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.surname)
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "home").send_keys(contact.phone)
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.NAME, "address2").send_keys(contact.address)
        self.driver.find_element(By.NAME, "submit").click()

    def open_contact_page(self):
        self.driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, username, password):
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
