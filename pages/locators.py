from selenium.webdriver.common.by import By


class MainPageLocators():
    # tuple (how, what) обернули в переменную LOGIN_LINK=(кортеж) содержащий сss и сам селектор искомого элемента стр.
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
