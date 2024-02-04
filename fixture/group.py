from selenium.webdriver.common.by import By
from pytest_training.model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(
                driver.find_elements(By.NAME, "new")) > 0):
            driver.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element(By.NAME, "update").click()
        self.open_groups_page()
        self.group_cache = None

    def count(self):
        self.open_groups_page()
        driver = self.app.driver
        return len(driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements(By.CSS_SELECTOR, 'span.group'):
                text = element.text
                group_id = element.find_element(By.NAME,
                                                "selected[]").get_attribute(
                    "value")
                self.group_cache.append(Group(name=text, id=group_id))
        return list(self.group_cache)
