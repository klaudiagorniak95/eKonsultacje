class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

        # WebElements for loginPage

        self.login_input = "//input[@id='login'][@name='login']"
        self.password_input = "//input[@id='password'][@name='password']"
        self.submit_button = "//button[@class='ladda-button btn btn-lg btn-primary'][@type='submit']"

    # methods for loginPage

    def enter_login(self, login):
        self.driver.find_element_by_xpath(self.login_input).clear()
        self.driver.find_element_by_xpath(self.login_input).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_input).clear()
        self.driver.find_element_by_xpath(self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    # test Steps for loginPage

    def user_login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_login()
