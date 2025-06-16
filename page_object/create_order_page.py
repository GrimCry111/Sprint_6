from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
import allure

class CreateOrderPage(BasePage):

    input_name=[By.XPATH, "//input[@placeholder='* Имя']"]
    input_surname=[By.XPATH, "//input[@placeholder='* Фамилия']"]
    input_address=[By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    button_metro=[By.XPATH, "//input[@placeholder='* Станция метро']"]
    choose_metro=[By.XPATH, "//div[text()='Черкизовская']"]
    input_phone=[By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next_step=[By.CLASS_NAME,"Button_Middle__1CSJM" ]

    button_calendar=[By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    week_on_calendar=[By.CLASS_NAME, "react-datepicker__week"]
    date_on_week=[By.CLASS_NAME, "react-datepicker__day"]
    button_rent=[By.CLASS_NAME, 'Dropdown-placeholder']
    choose_type_of_rent=[By.XPATH, "//div[text()='сутки']"]
    choose_color=[By.CLASS_NAME,'Checkbox_Label__3wxSf']
    input_comment=[By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    button_confirm=[By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[contains(text(), 'Заказ')]"]

    button_ok_confirm=[By.XPATH, "//button[text()='Да']"]

    button_look_status=[By.XPATH, "//button[text()='Посмотреть статус']"]


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Введём тестовое имя')
    def set_name(self):
        self.enter_text(self.input_name,'Иван')

    @allure.step('Введём тестовую фамилию')
    def set_surname(self):
        self.enter_text(self.input_surname,'Иванов')

    @allure.step('Введём тестовый адрес')
    def set_address(self):
        self.enter_text(self.input_address,'Тестовый адрес')

    @allure.step('Нажмём на поле Метро, чтобы увидеть список метро')
    def click_metro(self):
        self.click_to_element(self.button_metro)

    @allure.step('Выберем один из вариантов метро')
    def choose_first_metro(self):
        self.click_to_element(self.choose_metro)

    @allure.step('Введём тестовый номер телефона')
    def set_phone(self):
        self.enter_text(self.input_phone,'89998887766')

    @allure.step('Заполним первый шаг оформления заказа')
    def complete_first_step(self):
        self.set_name()
        self.set_surname()
        self.set_address()
        self.click_metro()
        self.choose_first_metro()
        self.set_phone()

    @allure.step('Нажмём на кнопку Далее, чтобы перейти ко второму шагу')
    def click_to_next_step(self):
        self.click_to_element(self.button_next_step)

    @allure.step('Нажмём на поле Календарь, чтобы увидеть доступные даты')
    def click_calendar(self):
        self.click_to_element(self.button_calendar)

    @allure.step('Выберем первую дату из доступных')
    def click_to_first_day(self, index):
        self.click_to_element_by_index(self.date_on_week , index)

    @allure.step('Нажмём на поле Аренда, чтобы увидеть доступные типы аренды')
    def click_to_rent(self):
        self.click_to_element(self.button_rent)

    @allure.step('Выберем один из вариантов аренды')
    def choose_first_type_of_rent(self):
        self.click_to_element(self.choose_type_of_rent)


    @allure.step('Выберем один из доступных цветов')
    def click_to_color(self,index):
        self.click_to_element_by_index(self.choose_color,index)

    @allure.step('Введём тестовый комментарий')
    def set_comment(self):
        self.enter_text(self.input_comment,'Тестовый комментарий')

    @allure.step('Заполним второй шаг оформления заказа')
    def complete_second_step(self):
        self.click_calendar()
        self.click_to_first_day(0)
        self.click_to_rent()
        self.choose_first_type_of_rent()
        self.click_to_color(0)
        self.set_comment()
    
    @allure.step('Нажмём кнопку Завершения оформления')
    def click_to_compete_order(self):
        self.click_to_element(self.button_confirm)

    @allure.step('Нажмём кнопку подтверждения оформелния')
    def click_to_confirm(self):  
        self.click_to_element(self.button_ok_confirm) 

    @allure.step('Нажмём кнопку, чтобы увидеть оформленный заказ')
    def click_to_show_order(self):
        self.click_to_element(self.button_look_status)  

    @allure.title('Заполняем данные по заказу')
    def complete_order(self):
        self.complete_first_step()
        self.click_to_next_step()
        self.complete_second_step()
        self.click_to_compete_order()
        self.click_to_confirm()
        self.click_to_show_order()
        self.assert_page("https://qa-scooter.praktikum-services.ru/track")
