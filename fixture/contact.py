from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.open_contact_page()
        driver = self.app.driver
        driver.find_element(By.NAME, "firstname").send_keys(contact.name)
        driver.find_element(By.NAME, "lastname").send_keys(contact.surname)
        driver.find_element(By.NAME, "company").send_keys(contact.company)
        driver.find_element(By.NAME, "home").send_keys(contact.phone)
        driver.find_element(By.NAME, "email").send_keys(contact.email)
        driver.find_element(By.NAME, "address2").send_keys(contact.address)
        driver.find_element(By.NAME, "submit").click()
        self.open_contact_page()

    def open_contact_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    def delete_first_contact(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#content > form:nth-child(10) > div:nth-child(8) "
                            "> input[type=button]").click()
        driver.switch_to.alert.accept()
