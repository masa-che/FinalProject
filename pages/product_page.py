from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage(BasePage):
    def checking_promo_url(self):
        # проверка promo в url
        promo_fragment = self.url.find("?promo=")
        assert promo_fragment > 0, "URL is not corrected"

    def add_to_basket(self):
        try:                                 # обработка возможной ошибки (кнопка отсутствует или не работает)
            self.browser.find_element(*ProductPageLocators.ADD_TO_BSK_BTN).click()
            return True
        except NoSuchElementException:       # в except указывается тип исключения который необходимо обработать
            return False

    def alert_field_add_to_basket(self):     # проверка появления поля о добавлении товара в корзину
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET), " Message isn't presented "

        # если браузеру не хватает времени чтобы найти css элемент из первого варианта кода, используй WebDriverWait!

        # WebDriverWait(self.browser, 20).until(
        #     expected_conditions.presence_of_element_located(ProductPageLocators.MESSAGE_ADD_BASKET))
        # try:
        #     return str(self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET).text)
        # except NoSuchElementException:
        #     return None

    def alert_field_price_to_basket(self):                # проверка появления поля со стоимостью корзины
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET), " Message isn't presented "

    def price_check(self):                                # проверка равенства цены указанной в алёрт окне и цены товара
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_book_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_ALERT).text
        assert price_book == price_book_in_alert, "wrong goods price, check basket sum or price of goods"

    def product_name_check(self):                         # проверка названий товаров в алёрт окне и описании товара
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_book_in_alert = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_ALERT).text
        assert name_book == name_book_in_alert, "wrong goods name, check the values in selectors"

    def should_not_be_alert_add_to_basket(self):          # проверка отсутствия алёрт окна о добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_BASKET),\
            "Success message is presented"

    def should_be_disappeared_alert_add_to_basket(self):  # проверка исчезание алерт окна добавления товара в корзину
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_BASKET),\
            "Success message is presented, should be disappeared"



