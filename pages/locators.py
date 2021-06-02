from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    REG_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.fade.in div.alertinner.wicon")

class ProductPageLocators():
    BUTTON_FIND = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner :nth-child(1) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_LINK_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    ICON_USER = (By.CSS_SELECTOR, "i.icon-user")

class BasketPageLocators():
    BASKET_PRODUCT = (By.CSS_SELECTOR, "#id_form-0-quantity")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")








