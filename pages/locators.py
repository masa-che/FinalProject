from selenium.webdriver.common.by import By


class MainPageLocators():
    # tuple (how, what) обернули в переменную LOGIN_LINK содержащий сss и сам селектор, страница main_page
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # кортеж (локатор,значение) для проверок присутствия форм логина и регистрации, на странице login_page
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    # кортеж (локатор,значение) для выбора продукта, добавления его в корзину и т.д, на странице product_page
    ADD_TO_BSK_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_ADD_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in")


