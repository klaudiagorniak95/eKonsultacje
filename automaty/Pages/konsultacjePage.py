from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from automaty.Pages.homePage import HomePage

class KonsultacjePage(object):

    def __init__(self, driver):
        self.driver = driver

        # instance of homePage method used for creating a new title for konsultacja (adding unique number to title)
        self.title_number = HomePage(self.driver).find_last_title_number()


        # WebElements for konsultacjePage

        self.nowa_button = '//button[@type="button"][@class="mb-2 mr-2 btn-icon btn btn-success"]'
        self.tytul_input = '//input[@id="title"][@name="title"]'
        self.tryb_radio = {'1': '//div[@class="form-check"]//label[@for="mode-0"]',
                                 '2': '//div[@class="form-check"]//label[@for="mode-1"]',
                                 '3': '//div[@class="form-check"]//label[@for="mode-2"]'}
        self.jednostka_select = '//select[@id="officeId"]'
        self.kategoria_select = '//select[@id="thematicAreaId"]'
        self.opis_textarea = '//textarea[@id="description"]'
        self.data_rozpoczecia_input = '//input[@type="text"][@id="dateFrom"]'
        self.data_zakonczenia_input = '//div[@class="react-datepicker-wrapper"]//input[@type="text"][@id="dateTo"]'

        # WebElements for konsulatacjaPage = dodaj nową formę

        self.nowa_forma_button = \
            '//div[@id="addConsultationFormButton"]//button[@type="button"][text()="Dodaj nową formę"]'
        self.sonda_button = \
            '//button[@class="btn-icon-vertical btn-transition btn btn-outline-primary"][text()="Sonda"]'
        self.ankieta_button = \
            '//button[@class="btn-icon-vertical btn-transition btn btn-outline-secondary"][text()="Ankieta"]'
        self.komentarz_button = \
            '//button[@class="btn-icon-vertical btn-transition btn btn-outline-success"][text()="Komentarze"]'

        # WebElements for konsultacjaPage = edytuj sondę

        self.sonda_edycja_button = '//button[@title="Edytuj formę konsultacji"]'
        self.sonda_opis_textarea = '//body[@class="modal-open"]//textarea[@id="shortDescription"]'
        self.sonda_data_rozpoczecia_input = '//body[@class="modal-open"]//input[@id="voteFrom"]'
        self.sonda_data_zakonczenia_input = '//body[@class="modal-open"]//input[@id="voteTo"]'
        self.sonda_tresc_pytania_input = '//input[@id="categories.0.questions.0.content"]'
        self.sonda_pokaz_odpowiedzi_button = '//body[@class="modal-open"]//button[@id="toggler-0"]'
        self.sonda_dodaj_odpowiedz_button = \
            '//body[@class="modal-open"]//button[@class="mr-2 btn-icon btn btn-success"]'
        self.sonda_tresc_odpowiedzi_input = '//div[@class="modal-content"]//input[@id="content"]'
        self.sonda_zatwierdz_odpowiedz_button = \
            '//div[@class="modal-content"]//div[@class="modal-footer"]//button[@type="submit"][text()="Dodaj"]'
        self.sonda_zapisz_button = '//div[@class="modal-footer"]//button[@type="submit"][text()="Zapisz"]'

        # WebElements = utworz

        self.konsultacja_utworz_button = '//form[@method="post"]//button[@type="submit"]'

    # methods for konsultacjePage

    def nowa_konsultacja(self):
        self.driver.find_element_by_xpath(self.nowa_button).click()

    def tytul_konsultacji(self):
        self.title = "KonsultacjaTestKG " + str(self.title_number)
        self.driver.find_element_by_xpath(self.tytul_input).clear()
        self.driver.find_element_by_xpath(self.tytul_input).send_keys(self.title)

    def tryb_konsultacji(self, tryb='1'):
        self.driver.find_element_by_xpath(self.tryb_radio[tryb]).click()

    def kategoria_konsultacji(self):
        Select(self.driver.find_element_by_xpath(self.kategoria_select)).select_by_visible_text("Kultura")

    def jednostka_konsultacji(self):
        Select(self.driver.find_element_by_xpath(self.jednostka_select)).select_by_value("1")

    def data_od_kosultacji(self, data_od):
        self.driver.find_element_by_xpath(self.data_rozpoczecia_input).send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.data_rozpoczecia_input).send_keys(data_od)
        self.driver.find_element_by_xpath(self.data_rozpoczecia_input).send_keys(Keys.ENTER)

    def data_do_konsultacji(self, data_do):
        self.driver.find_element_by_xpath(self.data_zakonczenia_input).send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.data_zakonczenia_input).send_keys(data_do)
        self.driver.find_element_by_xpath(self.data_zakonczenia_input).send_keys(Keys.ENTER)

    def opis_konsultacji(self, opis="Testowy opis konsultacji"):
        self.driver.find_element_by_xpath(self.opis_textarea).clear()
        self.driver.find_element_by_xpath(self.opis_textarea).send_keys(opis)

    def nowa_forma_konsultacja(self):
        self.driver.find_element_by_xpath(self.nowa_forma_button).click()

    def wybierz_sonde_konsultacja(self):
        self.driver.find_element_by_xpath(self.sonda_button).click()

    def edycja_sondy_konsultacja(self):
        self.driver.find_element_by_xpath(self.sonda_edycja_button).click()

    def sonda_opis_konsultacja(self, opis_sonda="Testowy opis sondy"):
        self.driver.find_element_by_xpath(self.sonda_opis_textarea).clear()
        self.driver.find_element_by_xpath(self.sonda_opis_textarea).send_keys(opis_sonda)
        self.driver.find_element_by_xpath(self.sonda_data_zakonczenia_input).send_keys(Keys.ENTER)

    def sonda_do_konsultacja(self, data_do):
        self.driver.find_element_by_xpath(self.sonda_data_zakonczenia_input).send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.sonda_data_zakonczenia_input).send_keys(data_do)
        self.driver.find_element_by_xpath(self.sonda_data_zakonczenia_input).send_keys(Keys.ENTER)

    def sonda_tresc_pytania(self, pytanie="Gdzie wolisz spędzać urlop?"):
        self.driver.find_element_by_xpath(self.sonda_tresc_pytania_input).clear()
        self.driver.find_element_by_xpath(self.sonda_tresc_pytania_input).send_keys(pytanie)

    def sonda_pokaz_odpowiedzi(self):
        self.driver.find_element_by_xpath(self.sonda_pokaz_odpowiedzi_button).click()

    def sonda_dodaj_odpowiedz(self):
        self.driver.find_element_by_xpath(self.sonda_dodaj_odpowiedz_button).click()

    def sonda_tresc_odpowiedzi(self, odpowiedz):
        self.driver.find_element_by_xpath(self.sonda_tresc_odpowiedzi_input).clear()
        self.driver.find_element_by_xpath(self.sonda_tresc_odpowiedzi_input).send_keys(odpowiedz)

    def sonda_zatwierdz_odpowiedz(self):
        self.driver.find_element_by_xpath(self.sonda_zatwierdz_odpowiedz_button).click()

    def sonda_zapisz(self):
        self.driver.find_element_by_xpath(self.sonda_zapisz_button).click()

    def utworz_konsultacje_button(self):
        self.driver.find_element_by_xpath(self.konsultacja_utworz_button).click()

    # steps for konsutlacjePage

    def wypelnij_pola_wymagane(self, data_od, data_do):
        self.nowa_konsultacja()
        self.tytul_konsultacji()
        self.tryb_konsultacji()
        self.jednostka_konsultacji()
        self.kategoria_konsultacji()
        self.opis_konsultacji()
        self.data_od_kosultacji(data_od)
        self.data_do_konsultacji(data_do)

    def nowa_sonda_konsultacja(self, data_do):
        self.nowa_forma_konsultacja()
        self.wybierz_sonde_konsultacja()
        self.edycja_sondy_konsultacja()
        self.sonda_opis_konsultacja()
        self.sonda_do_konsultacja(data_do)
        self.sonda_tresc_pytania()
        self.sonda_pokaz_odpowiedzi()
        self.odpowiedz = ['gory', 'morze']
        for i in range(len(self.odpowiedz)):
            self.sonda_dodaj_odpowiedz()
            self.sonda_tresc_odpowiedzi(self.odpowiedz[i])
            self.sonda_zatwierdz_odpowiedz()
        self.sonda_zapisz()

    def utworz_konsultacje(self):
        self.utworz_konsultacje_button()