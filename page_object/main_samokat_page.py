from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainSamokatPage:

    questions = [By.CLASS_NAME, 'accordion__item']
    text_questions = [By.CLASS_NAME, "accordion__panel"]
    cookie_button = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        self.driver = driver

    def close_banner(self):
        self.driver.find_element(*self.cookie_button).click()

    def find_all_questions(self):
        return self.driver.find_elements(*self.questions)

    def click_to_question(self,index):
        self.driver.find_elements(*self.questions)[index].click()

    def check_visible_of_question(self, index):
        # Найти все панели аккордеона
        panels = self.driver.find_elements(*self.text_questions)
        # Выбрать нужную панель по индексу
        panel = panels[index]
        # Ожидать видимости панели
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(panel),
            message=f"Панель вопроса {index} не открыта"
        )
        # Вернуть текст панели
        print(panel.text.strip())
        return panel.text.strip()