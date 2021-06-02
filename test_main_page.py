from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    #Метод проверяет, на странице содержится ли ссылка для перехода на страницу авторизации
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    #Метод проверяет возможность пользователя без авторизации перейти на стсраницу авторизации
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

#Метод проверяет отсутствие товаров в корзине, открытой с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    Basket_page = BasketPage(browser, browser.current_url)
    Basket_page.should_be_text_basket_is_empty()
    Basket_page.should_not_be_product()



