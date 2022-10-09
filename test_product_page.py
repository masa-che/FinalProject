from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()                                     # переход браузера по url
    product_page.checking_promo_url()                       # проверка на действие промоакции
    product_page.add_to_basket()                            # нажатие кнопки добавления товара в корзину
    product_page.solve_quiz_and_get_cod()                   # функция мат. расчёта (код написан при помощи selenium)
    product_page.assert_field_add_to_basket()               # проверка alert окна-добавления товара в корзину
    product_page.assert_field_price_to_basket()             # проверка alert окна-собщение со стоимостью корзины
    # book_name = product_page. # возврат_названия_книги()
    # book_price = product_page. # возврат_цены_книги()
    # product_page. # сообщение о успешной операции добавления в корзину товара(book_name, book_price)