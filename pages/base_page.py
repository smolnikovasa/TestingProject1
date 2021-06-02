import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    #Инициализация объекта
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    #Открытие пользователя
    def open(self):
        self.browser.get(self.url)

    #Проверка отображния элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    #Переход на страницу авторизации
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    #Проверка наличия ссылки для перехода на страницу авторизации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Нет ссылки на страницу авторизации"

    #Переход в корзиину
    def go_to_basket(self):
        button = self.browser.find_element(*BasePageLocators.BUTTON_LINK_BASKET)
        button.click()

    #Метод проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print("Ожидание 4 сек")
            return True
        return False

    #Метод проверяет исчезновение элемента в течение заданного времени
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print("Ожидание 4 сек")
            return False
        return True

    #Вычисление проверочного кода для получения скидки на товар
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Промо код не найден")

    #Проверка: авторизован ли пользователь
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Значок пользователя не отображается," \
                                                                 " возможно пользователь не авторизован"

