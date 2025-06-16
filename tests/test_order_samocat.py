import allure

from page_object.main_samokat_page import MainSamokatPage
from page_object.create_order_page import CreateOrderPage

class TestOrderSamokat:
    
    @allure.title('Проверка оформления заказа по верхней кнопке')
    @allure.description('На странице ищем элемент кнопка "Заказать" и проверяем, что по ней можно пройти весь флоу оформления заказа')
    def test_up_button(self,open_main_page):
        driver = open_main_page
        home_page = MainSamokatPage(driver)
        order_page = CreateOrderPage(driver)
        assert(len(home_page.find_all_order_buttons())) == 2
        home_page.click_order_button(0)
        order_page.complete_order()

    @allure.title('Проверка оформления заказа по нижней кнопке')
    @allure.description('На странице ищем элемент кнопка "Заказать" и проверяем, что по ней можно пройти весь флоу оформления заказа')
    def test_under_button(self,open_main_page):
        driver = open_main_page
        home_page = MainSamokatPage(driver)
        order_page = CreateOrderPage(driver)       
        assert(len(home_page.find_all_order_buttons())) == 2
        home_page.click_order_button(1)
        order_page.complete_order()
