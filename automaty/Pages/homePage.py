from selenium.common.exceptions import NoSuchElementException

class HomePage(object):

    def __init__(self, driver):

        self.driver = driver

        # WebElements for homePage

        self.profile_button = '//button[@type="button"][@aria-haspopup="true"]'
        self.logout_button = '//button[@type="button"][text()="Wyloguj"]'

        # Web Elements for homePage - Menu

        self.menu_konsultacje = '//a[@class="metismenu-link"][@href="/konsultacje"][text()="Konsultacje"]'
        self.menu_budzetObywatelski = '//a[@class="metismenu-link"][text()="Budżet obywatelski"]'
        self.menu_budzet = '//a[@class="metismenu-link"][@href="/budzety"][text()="Budżet"]'
        self.menu_harmonogramy = '//a[@class="metismenu-link"][@href="/budzet/harmonogramy"]'
        self.menu_stronyPomocy = '//a[@class="metismenu-link"][@href="/budzet/strony"]'
        self.menu_projekty = '//a[@class="metismenu-link"][@href="/budzet/projekty"]'
        self.menu_glosowania = '//a[@class="metismenu-link"][@href="/budzet/glosowania"]'

        self.last_used_title = '//*[contains(text(),"TestKG ")]'


    # methods for HomePage

    def click_profile(self):
        self.driver.find_element_by_xpath(self.profile_button).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button).click()

    def click_konsultacje(self):
        self.driver.find_element_by_xpath(self.menu_konsultacje).click()

    """
    FUNC USED WITH CREATING UNIQUE PROJECT TITLES (creating sequence number)
    searching for the last used project title which contains string: "TestKG "\
    if there is one - func checks if there is an int after the string and then adds 1 to it\
    if there isn't - func returns 1 (it means that we're creating first project ever)
    """

    def find_last_title_number(self):
        try:
            title = self.driver.find_element_by_xpath(self.last_used_title).text
            return int((title.split(" "))[-1]) + 1
        except NoSuchElementException:
            return 1
