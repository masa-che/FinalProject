from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def expect_no_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), "dark side feel I"

    def expect_empty_message_in_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), "basket isn't empty"

