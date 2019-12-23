import os, time, unittest, sys
from automaty.Pages.loginPage import LoginPage
from automaty.Pages.homePage import HomePage
from automaty.Pages.konsultacjePage import KonsultacjePage
from automaty.Tests.base import Base


class Konsultacja(Base):

    def testKonsultacje(self):
        l = LoginPage(self.driver)
        l.user_login('k.gorniak@sputnik.pl', 'Sputnik123')
        k = HomePage(self.driver)
        k.click_konsultacje()
        k = KonsultacjePage(self.driver)
        k.wypelnij_pola_wymagane()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        k.nowa_sonda_konsultacja()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        k.utworz_konsultacje()
        time.sleep(3)



if __name__ == '__main__':
    unittest.main()