class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element_by_index(self,locator,index):
        return self.driver.find_elements(*locator)[index]

    def click_to_element(self,locator):
        self.driver.find_element(*locator).click()

    def click_to_element_by_index(self,locator,index):
        self.driver.find_elements(*locator)[index].click()

    def enter_text(self,locator,enter_text):
        self.driver.find_element(*locator).send_keys(enter_text)

    def assert_page(self,url):
        assert url in self.driver.current_url