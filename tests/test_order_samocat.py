import allure

from page_object import main_samokat_page
from page_object import create_order_page

class TestOrderSamokat:
    
    @allure.title('Заполняем данные по заказу')
    def complete_order(self):
        self.order_page.complete_first_step()
        self.order_page.click_to_next_step()
        self.order_page.complete_second_step()
        self.order_page.click_to_compete_order()
        self.order_page.click_to_confirm()
        self.order_page.click_to_show_order()
        assert "https://qa-scooter.praktikum-services.ru/track" in self.driver.current_url

    @allure.title('Проверка оформления заказа по верхней кнопке')
    @allure.description('На странице ищем элемент кнопка "Заказать" и проверяем, что по ней можно пройти весь флоу оформления заказа')
    def test_up_button(self,open_main_page):
        self.driver = open_main_page
        self.home_page = main_samokat_page.MainSamokatPage(self.driver)
        self.order_page = create_order_page.CreateOrderPage(self.driver)
        assert(len(self.home_page.find_all_order_buttons())) == 2
        self.home_page.click_order_button(0)
        self.complete_order()

    @allure.title('Проверка оформления заказа по нижней кнопке')
    @allure.description('На странице ищем элемент кнопка "Заказать" и проверяем, что по ней можно пройти весь флоу оформления заказа')
    def test_under_button(self,open_main_page):
        self.driver = open_main_page
        self.home_page = main_samokat_page.MainSamokatPage(self.driver)
        self.order_page = create_order_page.CreateOrderPage(self.driver)
        assert(len(self.home_page.find_all_order_buttons())) == 2
        self.home_page.click_order_button(1)
        self.complete_order()
