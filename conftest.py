import pytest 
import allure
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
@allure.step('Открываем страницу')
def open_main_page(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    return driver
