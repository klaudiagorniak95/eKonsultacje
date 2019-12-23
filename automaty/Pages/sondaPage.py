from automaty.Locators.locators import Locators
from selenium.webdriver.support.ui import Select

class SondaPage(object):

    def __init__(self, driver):
        self.driver = driver

        # WebElements for konsultacjePage

        self.sonda_trescPytania = ''