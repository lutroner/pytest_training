from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").send_keys(
            group.header)
        driver.find_element(By.NAME, "group_footer").send_keys(
            group.footer)
        driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.NAME, "delete").click()
        self.open_groups_page()
