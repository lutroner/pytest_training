from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 600)
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)

    def create_group(self, group):
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").send_keys(
            group.header)
        self.driver.find_element(By.NAME, "group_footer").send_keys(
            group.footer)
        self.driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
