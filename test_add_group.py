from selenium import webdriver
from selenium.webdriver.common.by import By

from group import Group


class TestAddGroup:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 600)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(
            Group(name="Бегимоты", header="Живут", footer="В болоте"))
        self.open_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name="", header="", footer=""))
        self.open_groups_page()
        self.logout()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, group):
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").send_keys(
            group.header)
        self.driver.find_element(By.NAME, "group_footer").send_keys(
            group.footer)
        self.driver.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
