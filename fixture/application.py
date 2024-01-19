from selenium import webdriver

from pytest_training.fixture.contact import ContactHelper
from pytest_training.fixture.group import GroupHelper
from pytest_training.fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 600)
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
