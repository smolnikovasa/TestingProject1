from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    #Проверка содержания тсраницы
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма входа не присутствует на странице"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не присутствует на странице"


    #Проверяем присутствует ли кнопка регистрации пользователя на странице
    def should_be_button(self):
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), \
            "Кнопка регистрации пользователя не отображается на странице"

   #Осуществление регистрации нового пользователя
    def register_new_user(self, email, password):
        self.should_be_button()
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_password.send_keys(password)
        reg_password2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2)
        reg_password2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_btn.click()
        self.should_be_success_message()

    #Проверка отображения сообщения об успешной реистрации пользователя
    def should_be_success_message(self):
        assert self.is_element_present(*LoginPageLocators.REG_SUCCESS_MESSAGE), \
            "На странице не появилось сообщение об успешной регистсрации пользователя"




