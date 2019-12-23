import time, unittest
from automaty.Pages.loginPage import LoginPage
from automaty.Pages.homePage import HomePage
from automaty.Pages.konsultacjePage import KonsultacjePage
from automaty.Tests.base import Base
from datetime import datetime, timedelta

class Konsultacja(Base):

    start_day = datetime.today().strftime('%Y-%m-%d')
    end_day = datetime.strftime(datetime.now() + timedelta(30), '%Y-%m-%d')


    def testKonsultacje(self):
        l = LoginPage(self.driver)
        l.user_login('********', '*****')
        h = HomePage(self.driver)
        h.click_konsultacje()
        h.find_last_title_number()
        k = KonsultacjePage(self.driver)
        k.wypelnij_pola_wymagane(self.start_day, self.end_day)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        k.nowa_sonda_konsultacja(self.end_day)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        k.utworz_konsultacje()
        time.sleep(10)

if __name__ == '__main__':
    unittest.main()