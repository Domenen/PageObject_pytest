from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    
    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK
        ), "Нет кнопки войти"


    def go_to_login_page(self):
        link = self.browser.find_element(
            *MainPageLocators.LOGIN_LINK
        )
        link.click()
