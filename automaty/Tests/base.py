import unittest
from selenium import webdriver
import os
class Base(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.dir = os.path.dirname(__file__)
        cls.chrome_driver_path = cls.dir + "\chromedriver.exe"
        cls.driver = webdriver.Chrome(cls.chrome_driver_path)
        cls.driver.maximize_window()
        cls.driver.get('https://test-ekonsultacje-bo.eboi.pl:8101/')
        cls.driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()