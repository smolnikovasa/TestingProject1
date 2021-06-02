from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException



class ProductPage(BasePage):
    #Добавляем товар в корзину
    def add_product_to_cart(self):
        self.should_be_promo_link("promo")
        self.should_be_button()
        button_add_product_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_FIND)
        button_add_product_to_cart.click()
        self.solve_quiz_and_get_code()

    #Определяем название добавляемого в корзину товара
    def product_name(self):
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        except NoSuchElementException:
            return None, "Товар не определен"

    #Определяем цену добавляемого в корзину товара
    def product_price(self):
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        except NoSuchElementException:
            return None, "Цена товаране определена"

    #Проверяем присутствует ли кнопка добавления товара в корзину на странице
    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_FIND), "Кнопка добавления товара в корзину не присутствует на странице"

    #Ссылка на товар содержжит ли специальный промо параметр
    def should_be_promo_link(self, promo):
        assert promo in self.url, "Промо параметр не содержится в веб адресе"

    #Проверка присутствия сообщения об успешном добавлении товара в корзину на странице
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "На странице не появилось сообщение об успешном добавлении товара в корзину"

    #Метод проверяет, что сообщения об успешном добавлении товара в корзину не появляется в течении заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "На странице появилось сообщение об успешном добавлении товара в корзину, которого не должно быть"

    #Проверка пропадения сообщения через определенный промежуток времени
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении товара в корзину сначала появилось, а позже пропало"

    #Проврка корректности информации о добавленном в корзину товаре
    def should_info_of_product_is_correct(self, product_name, product_price):
        print(f"Добавление товара {product_name} с ценой {product_price } в корзину")
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text.strip()
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text.strip()
        print(f"Информация о цене товара {basket_product_price}")
        print(f"Информация о Товаре {basket_product_name}")
        assert (product_price == basket_product_price) and (product_name == basket_product_name), \
            "Информация о товаре в корзине некорректна"


