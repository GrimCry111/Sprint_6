from selenium import webdriver

from page_object import main_samokat_page

class TestOrderSamokat:
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.home_page = main_samokat_page.MainSamokatPage(cls.driver)


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit() 