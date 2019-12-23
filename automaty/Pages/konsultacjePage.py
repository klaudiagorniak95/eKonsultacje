from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class KonsultacjePage(object):

    def __init__(self, driver):
        self.driver = driver


        # WebElements for konsultacjePage

        self.konsultacja_nowa = '//button[@type="button"][@class="mb-2 mr-2 btn-icon btn btn-success"]'
        self.konsultacja_tytul = '//input[@id="title"][@name="title"]'
        self.konsultacja_tryb = {'1': '//div[@class="form-check"]//label[@for="mode-0"]',
                                 '2': '//div[@class="form-check"]//label[@for="mode-1"]',
                                 '3': '//div[@class="form-check"]//label[@for="mode-2"]'}
        self.konsultacja_jednostka = '//select[@id="officeId"]'
        self.konsultacja_kategoria = '//select[@id="thematicAreaId"]'
        self.konsultacja_opis = '//textarea[@id="description"]'
        self.konsultacja_dataOd = '//input[@type="text"][@id="dateFrom"]'
        self.konsultacja_dataDo = '//div[@class="react-datepicker-wrapper"]//input[@type="text"][@id="dateTo"]'

        # WebElements for konsulatacjaPage = dodaj nową formę

        self.konsultacja_nowaForma = \
            '//div[@id="addConsultationFormButton"]//button[@type="button"][text()="Dodaj nową formę"]'
        self.konsultacja_sonda = \
            '//button[@class="btn-icon-vertical btn-transition btn btn-outline-primary"][text()="Sonda"]'
        self.konsultacja_ankieta = \
            '//button[@class="btn-icon-vertical btn-transition btn btn-outline-secondary"][text()="Ankieta"]'
        self.konsultacja_komentarze = \
            '//button[@class="btn-icon-vertical btn-transition btn btn-outline-success"][text()="Komentarze"]'

        # WebElements for konsultacjaPage = edytuj sondę

        self.konsultacja_sondaEdycja = '//button[@title="Edytuj formę konsultacji"]'
        self.konsultacja_sondaOpis = '//body[@class="modal-open"]//textarea[@id="shortDescription"]'
        self.konsultacja_sondaOd = '//body[@class="modal-open"]//input[@id="voteFrom"]'
        self.konsultacja_sondaDo = '//body[@class="modal-open"]//input[@id="voteTo"]'
        self.konsultacja_sondaTrescPytania = '//input[@id="categories.0.questions.0.content"]'
        self.konsultacja_sondaPokazOdpowiedzi = '//body[@class="modal-open"]//button[@id="toggler-0"]'
        self.konsultacja_sondaDodajOdpowiedz = \
            '//body[@class="modal-open"]//button[@class="mr-2 btn-icon btn btn-success"]'
        self.konsultacja_sondaTrescOdpowiedzi = '//div[@class="modal-content"]//input[@id="content"]'
        self.konsultacja_sondaZatwierdzOdpowiedz = \
            '//div[@class="modal-content"]//div[@class="modal-footer"]//button[@type="submit"][text()="Dodaj"]'
        self.konsultacja_sondaZapisz = '//div[@class="modal-footer"]//button[@type="submit"][text()="Zapisz"]'

        # WebElements = utworz

        self.konsultacja_utworz = '//form[@method="post"]//button[@type="submit"]'

    # methods for konsultacjePage

    def nowa_konsultacja(self):
        self.driver.find_element_by_xpath(self.konsultacja_nowa).click()

    def tytul_konsultacji(self, tytul='Konsultacja testowa KG'):
        self.driver.find_element_by_xpath(self.konsultacja_tytul).clear()
        self.driver.find_element_by_xpath(self.konsultacja_tytul).send_keys(tytul)

    def tryb_konsultacji(self, tryb='1'):
        self.driver.find_element_by_xpath(self.konsultacja_tryb[tryb]).click()

    def kategoria_konsultacji(self):
        Select(self.driver.find_element_by_xpath(self.konsultacja_kategoria)).select_by_visible_text("Kultura")

    def jednostka_konsultacji(self):
        Select(self.driver.find_element_by_xpath(self.konsultacja_jednostka)).select_by_value("1")

    def data_do_konsultacji(self, data_do="2020-01-30"):
        self.driver.find_element_by_xpath(self.konsultacja_dataDo).send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.konsultacja_dataDo).send_keys(data_do)

    def opis_konsultacji(self, opis="Testowy opis konsultacji"):
        self.driver.find_element_by_xpath(self.konsultacja_opis).clear()
        self.driver.find_element_by_xpath(self.konsultacja_opis).send_keys(opis)

    def nowa_forma_konsultacja(self):
        self.driver.find_element_by_xpath(self.konsultacja_nowaForma).click()

    def wybierz_sonde_konsultacja(self):
        self.driver.find_element_by_xpath(self.konsultacja_sonda).click()

    def edycja_sondy_konsultacja(self):
        self.driver.find_element_by_xpath(self.konsultacja_sondaEdycja).click()

    def sonda_opis_konsultacja(self, opis_sonda="Testowy opis sondy"):
        self.driver.find_element_by_xpath(self.konsultacja_sondaOpis).clear()
        self.driver.find_element_by_xpath(self.konsultacja_sondaOpis).send_keys(opis_sonda)

    def sonda_do_konsultacja(self, data_do="2020-01-30"):
        self.driver.find_element_by_xpath(self.konsultacja_dataDo).send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.konsultacja_sondaDo).send_keys(data_do)

    def sonda_tresc_pytania(self, pytanie="Gdzie wolisz spędzać urlop?"):
        self.driver.find_element_by_xpath(self.konsultacja_sondaTrescPytania).clear()
        self.driver.find_element_by_xpath(self.konsultacja_sondaTrescPytania).send_keys(pytanie)

    def sonda_pokaz_odpowiedzi(self):
        self.driver.find_element_by_xpath(self.konsultacja_sondaPokazOdpowiedzi).click()

    def sonda_dodaj_odpowiedz(self):
        self.driver.find_element_by_xpath(self.konsultacja_sondaDodajOdpowiedz).click()

    def sonda_tresc_odpowiedzi(self, odpowiedz):
        self.driver.find_element_by_xpath(self.konsultacja_sondaTrescOdpowiedzi).clear()
        self.driver.find_element_by_xpath(self.konsultacja_sondaTrescOdpowiedzi).send_keys(odpowiedz)

    def sonda_zatwierdz_odpowiedz(self):
        self.driver.find_element_by_xpath(self.konsultacja_sondaZatwierdzOdpowiedz).click()

    def sonda_zapisz(self):
        self.driver.find_element_by_xpath(self.konsultacja_sondaZapisz).click()

    def utworz_konsultacje_button(self):
        self.driver.find_element_by_xpath(self.konsultacja_utworz).click()

    # steps for konsutlacjePage

    def wypelnij_pola_wymagane(self):
        self.nowa_konsultacja()
        self.tytul_konsultacji()
        self.tryb_konsultacji()
        self.jednostka_konsultacji()
        self.kategoria_konsultacji()
        self.opis_konsultacji()
        self.data_do_konsultacji()

    def nowa_sonda_konsultacja(self):
        self.nowa_forma_konsultacja()
        self.wybierz_sonde_konsultacja()
        self.edycja_sondy_konsultacja()
        self.sonda_opis_konsultacja()
        # self.sonda_do_konsultacja()
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