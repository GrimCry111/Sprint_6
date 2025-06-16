from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
import allure

class MainSamokatPage(BasePage):

    questions = [By.CLASS_NAME, 'accordion__item']
    text_questions = [By.CLASS_NAME, "accordion__panel"]
    cookie_button = [By.ID, 'rcc-confirm-button']
    new_order_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Убираем куки')
    def close_banner(self):
        self.click_to_element(self.cookie_button)

    @allure.step('Находим все вопросы на странице')
    def find_all_questions(self):
        return self.find_elements(self.questions)
    
    @allure.step('Кликаем на вопрос №{index}')
    def click_to_question(self,index):        
        self.click_to_element_by_index(self.questions,index)

    @allure.step('Получаем ответ на вопрос №{index}')
    def check_visible_of_question(self, index):
        panel = self.find_element_by_index(self.text_questions,index)
        return panel.text.strip()
    
    @allure.step('Найдём все кнопки на странице с текстом "Заказать"')
    def find_all_order_buttons(self):
        buttons = self.find_elements(self.new_order_button)
        matching_buttons = [btn for btn in buttons if btn.text.strip() == "Заказать"]
        return matching_buttons
    
    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self,index):
        buttons = self.find_all_order_buttons()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", buttons[index])
        self.driver.execute_script("arguments[0].click();", buttons[index])
        #self.click_to_element_by_index(self.new_order_button, index)