from .pages.product_page import ProductPage
import pytest


# фикстура с параметром введена для того, чтобы при прохождении теста по выборке из 9-ти link
# обнаруженная ошибка на "7" не останавливала ран теста?f проходила его до конца (задание 4.3.4 )
# @pytest.mark.parametrize('number', [pytest.param(x, marks=pytest.mark.xfail(x=7, reason='need to fix'))
# for x in range(10)])
# def test_guest_can_add_product_to_basket(browser, number):
# link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
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
    item_page.open()                                      # переход браузера по url
    item_page.add_to_basket()                             # нажатие кнопки добавления товара в корзину
    item_page.should_be_disappeared_alert_add_to_basket() # проверка исчезание алерт окна добавления товара в корзину
