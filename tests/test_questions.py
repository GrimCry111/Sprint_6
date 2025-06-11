from selenium import webdriver

from page_object import main_samokat_page

class TestQuestion:

    list_of_questions  = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                        'Да, обязательно. Всем самокатов! И Москве, и Московской области.']


    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.home_page = main_samokat_page.MainSamokatPage(cls.driver)

    def test_question(self):
        self.home_page.close_banner()
        count = len(self.home_page.find_all_questions())
        for index in range(0,count):
            print(index)
            self.home_page.click_to_question(index)
            actual_text = self.home_page.check_visible_of_question(index)
            assert actual_text == self.list_of_questions[index], \
                f"Ожидалось: {self.list_of_questions[index]}, получено: {actual_text}"


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit() 