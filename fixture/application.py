from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 600)
        self.driver.implicitly_wait(60)

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

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

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
