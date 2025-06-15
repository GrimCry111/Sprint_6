import allure

from page_object import main_samokat_page
from page_object import create_order_page

class TestOrderSamokat:
    
    @allure.title('Заполняем данные по заказу')
    def complete_order(self,driver):
        order_page = create_order_page.CreateOrderPage(driver)
        order_page.complete_first_step()
        order_page.click_to_next_step()
        order_page.complete_second_step()
        order_page.click_to_compete_order()
        order_page.click_to_confirm()
        order_page.click_to_show_order()
        assert "https://qa-scooter.praktikum-services.ru/track" in driver.current_url

    @allure.title('Проверка оформления заказа по верхней кнопке')
    @allure.description('На странице ищем элемент кнопка "Заказать" и проверяем, что по ней можно пройти весь флоу оформления заказа')
    def test_up_button(self,open_main_page):
        driver = open_main_page
        home_page = main_samokat_page.MainSamokatPage(driver)
        assert(len(home_page.find_all_order_buttons())) == 2
        home_page.click_order_button(0)
        self.complete_order(driver)

    @allure.title('Проверка оформления заказа по нижней кнопке')
    @allure.description('На странице ищем элемент кнопка "Заказать" и проверяем, что по ней можно пройти весь флоу оформления заказа')
    def test_under_button(self,open_main_page):
        driver = open_main_page
        home_page = main_samokat_page.MainSamokatPage(driver)       
        assert(len(home_page.find_all_order_buttons())) == 2
        home_page.click_order_button(1)
        self.complete_order(driver)
