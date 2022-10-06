from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException


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


    