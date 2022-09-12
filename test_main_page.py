from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):       # тест перехода на страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и урлу
    page.open()                                     # открываем страницу
    page.go_to_login_page()                         # выполняем метод(def) страницы - переходим на страницу логина


def test_guest_should_see_login_link(browser):      # проверка перехода по видимой (css-maine_page)  линке
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                  # для читабельности класс в переменную
    page.open()                                     # открытие страницы
    page.should_be_login_link()                     # проверка присутствия на странице линки к логину

