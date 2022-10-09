from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage(BasePage):
    def checking_promo_url(self):
        # проверка promo в url
        promo_fragment = self.url.find("?promo=newYear")
        assert promo_fragment > 0, "URL is not corrected"

    def add_to_basket(self):
        try:                                 # обработка возможной ошибки (кнопка отсутствует или не работает)
            self.browser.find_element(*ProductPageLocators.ADD_TO_BSK_BTN).click()
            return True
        except NoSuchElementException:       # в except указывается тип исключения который необходимо обработать
            return False

    def assert_field_add_to_basket(self):    # проверка появления поля о добавлении товара в корзину
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_BASKET), "Success message is presented"

        # если браузеру не хватает времени чтобы найти css элемент из первого варианта кода, используй WebDriverWait!

        # WebDriverWait(self.browser, 20).until(
        #     expected_conditions.presence_of_element_located(ProductPageLocators.MESSAGE_ADD_BASKET))
        # try:
        #     return str(self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET).text)
        # except NoSuchElementException:
        #     return None






