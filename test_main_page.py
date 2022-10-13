from .pages.main_page import MainPage
from .pages.login_page import LoginPage

import time


def test_guest_can_go_to_login_page(browser):       # тест перехода на страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и урлу
    page.open()                                     # открытие страницы по адресу link
    login_page = page.go_to_login_page()            # переход на страницу логина
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):      # проверка перехода по видимой (css-maine_page)  линке
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                  # для читабельности класс в переменную
    page.open()                                     # открытие страницы по адресу link
    page.should_be_login_link()                     # проверка присутствия на странице линки к логину


def test_login_and_registration_forms(browser):     # тест страницы registration and login (файл login_page)
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()                      # проверка  по url, что мы на странице registration and login
    page.should_be_login_form()                     # проверка присутствия на странице формы логина
    page.should_be_register_form()                  # проверка присутствия на странице формы регистрации


# pytest -v --tb=line --language=en test_main_page.py
