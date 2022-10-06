from .pages.product_page import ProductPage


# черновик
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()                            # нажатие кнопки добавления товара в корзину
    product_page.solve_quiz_and_get_cod()                   # функция мат. расчёта (код написан при помощи selenium)
    # book_name = product_page. # возврат_названия_книги()
    # book_price = product_page. # возврат_цены_книги()
    # product_page. # сообщение о успешной операции добавления в корзину товара(book_name, book_price)