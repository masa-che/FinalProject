from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import time
import pytest


# фикстура с параметром введена для того, чтобы при прохождении теста по выборке из 9-ти link
# обнаруженная ошибка на "7" не останавливала ран теста проходила его до конца (задание 4.3.4 )
# @pytest.mark.parametrize('number', [pytest.param(x, marks=pytest.mark.xfail(x=7, reason='need to fix'))
# for x in range(10)])
# def test_guest_can_add_product_to_basket(browser, number):
# link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()                                  # переход браузера по url
    product_page.checking_promo_url()                    # проверка на действие промоакции (правильный url)
    product_page.add_to_basket()                         # нажатие кнопки добавления товара в корзину
    product_page.solve_quiz_and_get_cod()                # функция мат. расчёта (код написан при помощи selenium)
    product_page.alert_field_add_to_basket()             # проверка alert окна-добавления товара в корзину
    product_page.alert_field_price_to_basket()           # проверка alert окна-собщение со стоимостью корзины
    product_page.price_check()                           # проверка равенства цены указанной в алёрт окне и цены товара
    product_page.product_name_check()                    # проверка названий товаров в алёрт окне и описании товара


@pytest.mark.xfail  # падает (негативная проверка)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()                                      # переход браузера по url
    item_page.add_to_basket()                             # нажатие кнопки добавления товара в корзину
    item_page.should_not_be_alert_add_to_basket()         # проверка отсутствия алёрт окна о добавлении товара в корзину


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()                                      # переход браузера по url
    item_page.should_not_be_alert_add_to_basket()         # проверка отсутствия алёрт окна о добавлении товара в корзину


@pytest.mark.xfail  # падает (негативная проверка)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()                                         # переход браузера по url
    item_page.add_to_basket()                                # нажатие кнопки добавления товара в корзину
    item_page.should_be_disappeared_alert_add_to_basket()    # проверка исчезание алерт окна добавления товара в корзину


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()                              # проверка присутствия login_link на product_page


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()                                  # проверка перехода на login_page из product_page


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    page = ProductPage(browser, link)                        # по заданию старт теста со страницы product
    page.open()                                              # открытие страницы по адресу url
    page.go_to_basket()                                      # переход в раздел basket
    basket_page = BasketPage(browser, browser.current_url)   # для работы методов используем обьект класса BasketPage
    basket_page.expect_no_goods_in_the_basket()              # проверка,что корзина пуста
    basket_page.expect_empty_message_in_the_basket()         # проверка сообщения, что корзина пуста


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:                   # 4.3.13 обьединение тестов в один класс, рег. пользователя
    @pytest.fixture(scope="function", autouse=True)         # autouse - запуск тестов без явного вызова фикстуры
    def setup(self, browser):                               # ВАЖНО! этот пример рассматривается в учебных целях, в работе не надо так ¯\_(ツ)_/¯
        link = "http://selenium1py.pythonanywhere.com//accounts/login/"
        login_page = LoginPage(browser, link)               # для регистрации пользователя берём метод из LoginPage
        login_page.open()                                   # открытие страницы регистрации по link
        email = str(time.time()) + "@fakemail.com"          # при помощи модуля time создаём email
        password = str(time.time())                         # при помощи модуля time создаём password
        login_page.register_new_user(email, password)       # регистрация пользователя, в метод парсятся имейл с паролем
        main_page = MainPage(browser, browser.current_url)  # для проверки в работу берём метод из MainPage с использованием текущей url (curent_url)
        main_page.check_authorized_user()                   # метод проверки регистрации пользователя

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()                                 # переход браузера по url
        product_page.add_to_basket()                        # нажатие кнопки добавления товара в корзину
        product_page.alert_field_add_to_basket()            # проверка alert окна-добавления товара в корзину
        product_page.alert_field_price_to_basket()          # проверка alert окна-собщение со стоимостью корзины
        product_page.price_check()                          # проверка равенства цены указанной в алёрт окне и цены товара
        product_page.product_name_check()                   # проверка названий товаров в алёрт окне и описании товара

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        item_page = ProductPage(browser, link)
        item_page.open()                                    # переход браузера по url
        item_page.should_not_be_alert_add_to_basket()       # проверка отсутствия алёрт окна о добавлении товара в корзину
