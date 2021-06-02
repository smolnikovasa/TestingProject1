import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest

#Тест проверяет возможность добавления товара в корзину гостем
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="найден баг")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.add_product_to_cart()
    page.should_info_of_product_is_correct(page.product_name().strip(), page.product_price().strip())


#Тест проверяет наличие сообщения об успехе после добавления товара в корзину
def test_guest_can_see_success_massage_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.add_product_to_cart()
    page.should_be_success_message()

#Тест проверяет отображение на экране сообщения о добавлении товара в корзину после открытия страницы
@pytest.mark.skip
def test_guest_can_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.should_be_success_message()

#Тест проверяет отображение на экране ссылки для перехода на страницу авторизации
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


#Тест проверяет отсутствие сообщения об успехе после успешного добавления товара в корзину
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

#Тест проверяет отсутстсвие сообщения о дообавлении товара в корзину после открытия страницы продукта
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.should_not_be_success_message()

#Тест проверяет появление сообщения об успехе после добавления товара в корзину и последующее исчезновение через неск сек
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.add_product_to_cart()
    page.should_disappeared_success_message()


#Тест проверяет возможность перехода на страницу авторизации со страницы товара
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


#Тест проверяет отсутствие продуктов в корзине, открытой со страницы товара
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    Basket_page = BasketPage(browser, browser.current_url)
    Basket_page.should_be_text_basket_is_empty()
    Basket_page.should_not_be_product()


class TestUserAddToBasketFromProductPage():

    #Создание пользователя, выполняется перед прохождением каждого из тестов
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "C12345678"
        page.register_new_user(email, password)
        page.should_be_success_message()
        page.should_be_authorized_user

    #Тест проверяет отсутствие сообщения об успешном добавлении товара в корзину на странце товара
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        print(link)
        page.open()
        page.should_not_be_success_message()

    #Тест проверяет возможность добавления товара в корзину под учеткой авторизованного пользователя
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        print(link)
        page.open()
        page.add_product_to_cart()
        page.should_info_of_product_is_correct(page.product_name().strip(), page.product_price().strip())


