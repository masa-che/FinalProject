from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и урлу
    page.open()                                     # открываем страницу
    page.go_to_login_page()                         # выполняем метод страницы - переходим на страницу логина




