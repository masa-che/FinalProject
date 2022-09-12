from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)       # неявное ожидание

    def open(self):
        self.browser.get(self.url)                  # открытие страницы по адресу в url

    def is_element_present(self, how, what):        # функция перехвата исключения (exception)
        try:                                        # выполняем инструкцию, которая может породить исключение
            self.browser.find_element(how, what)
        except NoSuchElementException:              # перехват самого исключения
            return False
        return True

# функцию is_element_present будем юзать в main_page
# (by.css_selector-how, "#селектор"-what) == (*MainPageLocators.LOGIN_LINK)

    