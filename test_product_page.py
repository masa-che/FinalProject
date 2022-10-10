from .pages.product_page import ProductPage


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


