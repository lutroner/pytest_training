from selenium.webdriver.common.by import By

from pytest_training.model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        driver.find_element(By.NAME, "submit").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("address2", contact.address)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)
        self.contact_cache = None

    def open_home_page(self):
        driver = self.app.driver
        if not driver.current_url.endswith("addressbook/"):
            self.app.open_home_page()

    def open_add_contact_page(self):
        driver = self.app.driver
        if not driver.current_url.endswith("/edit.php"):
            driver.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a').click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.select_contact_by_index(index)
        driver.find_element(By.CSS_SELECTOR,
                            "#content > form:nth-child(10) > div:nth-child(8) "
                            "> input[type=button]").click()
        driver.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def count(self):
        self.open_home_page()
        driver = self.app.driver
        return len(driver.find_elements(By.NAME, "entry"))

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.open_home_page()
        self.select_contact_by_index(index)
        driver.find_element(By.XPATH,
                            '//*[@id="maintable"]/tbody/tr[2]/td[8]').click()
        self.fill_contact_form(new_contact_data)
        driver.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_home_page()
            self.contact_cache = []
            for element in driver.find_elements(By.NAME, "entry"):
                text = element.text
                group_id = element.find_element(By.NAME,
                                                "selected[]").get_attribute(
                    "value")
                self.contact_cache.append(Contact(name=text, id=group_id))
        return list(self.contact_cache)
