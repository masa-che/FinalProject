from selenium.webdriver.common.by import By


class MainPageLocators:
    # tuple (how, what) обернули в переменную LOGIN_LINK содержащий сss и сам селектор, страница main_page
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # кортеж (локатор,значение) для проверок присутствия форм логина и регистрации пользователя, на странице login_page
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    # кортеж (локатор,значение) для выбора продукта, добавления его в корзину и т.д, на странице product_page
    ADD_TO_BSK_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_ADD_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK_IN_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    NAME_BOOK_IN_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")  # после использования локатора для теста, изменить на LOGIN_LINK
    MOVE_TO_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEMS_TO_BUY = (By.CSS_SELECTOR, ".basket-items")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner > p")
