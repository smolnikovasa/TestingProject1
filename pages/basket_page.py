from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT),\
            "В корзине содержатся товары, а их не должно быть"

    def should_be_text_basket_is_empty(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text,\
            "Нет надписи 'Ваша корзина пуста', но она должна быть"
