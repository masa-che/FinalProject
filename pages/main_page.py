from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
# закаменчено по условию переноса кода (задание 4.3.8) установлена заглушка def __init__
    # переход на страницу логина и регистрации пользоватнля
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)  # click "Войти или зарегистрироваться"
    #     link.click()
    #     # alert = self.browser.switch_to.alert    # часть кода для обхода алёртов на main page
    #     # alert.accept()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)
    #
    # def should_be_login_link(self):  # проверка присутствия самой линк
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

# конструкция *MainPageLocators.LOGIN_LINK -содержит ссылку на Класс-локаторов и переменную содержащую tuple (how, what)
# how  - аргумент КАК искать (xpath, id, class, css, etc)
# what - аргумент ЧТО искать (str-selector)

