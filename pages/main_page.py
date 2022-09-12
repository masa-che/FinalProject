from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):                                                # переход по линк
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)   # click по "Войти или зарегистрироваться"
        login_link.click()

    def should_be_login_link(self):                                            # проверка присутствия самой линк
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

# конструкция *MainPageLocators.LOGIN_LINK - содержит ссылку на Класс и переменную содержащую tuple (how, what)
# how  - аргумент КАК искать (xpath, id, class, css, etc)
# what - аргумент ЧТО искать (str-selector)
