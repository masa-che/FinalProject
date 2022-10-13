from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocators


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

    def solve_quiz_and_get_cod(self):                           # метод получения проверочного кода
        alert = self.browser.switch_to.alert                    # определение алёрт-окна и переключение на него
        x = alert.text.split(" ")[2]                            # парсит число присвоенное иксу
        answer = str(math.log(abs((12 * math.sin(float(x))))))  # вычисление с взятым из икса числом
        alert.send_keys(answer)                                 # добавление результата в окно алёрт
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")                     # вывод расчёта ф-ции в console
            alert.accept()
        except NoAlertPresentException:                        # если расчёт не состоялся выпадет exept
            print("Нет второго алерт-окна")

    # метод для негативных проверок
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # метод для негативных проверок
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # переход на страницу логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # проверка присутствия самой link
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
