from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):                                                 # переход по линк
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):                                             # проверка присутствия самой линк
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

# how  - аргумент КАК искать (xpath, id, class, css, etc)
# what - аргумент ЧТО искать (str-selector)
