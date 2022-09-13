from selenium.webdriver.common.by import By


class MainPageLocators():
    # tuple (how, what) обернули в переменную LOGIN_LINK содержащий сss и сам селектор, страница main_page
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # кортеж id и селектор для проверок присутствия форм логина и регистрации, на странице login_page
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form_")
