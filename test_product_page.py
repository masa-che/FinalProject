from .pages.base_page import BasePage
from .pages.locators import MainPageLocators
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.#add_to_basket()
    product_page.#solve_quiz_and_get_code()
    book_name = product_page.#return_book_name()
    book_price = product_page.#return_book_price()
    product_page.#should_be_success_message(book_name, book_price)