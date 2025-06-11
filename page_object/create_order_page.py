from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateOrderPage:

    input_name=[]
    input_surname=[]
    input_address=[]
    button_metro=[]
    choose_metro=[]
    input_phone=[]
    button_next_step=[]

    button_calendar=[]
    choose_date_on_calendar=[]
    button_rent=[]
    choose_type_of_rent=[]
    choose_color=[]
    input_comment=[]
    button_confirm=[]

    button_ok_confirm=[]

    button_look_status=[]


    def __init__(self, driver):
        self.driver = driver