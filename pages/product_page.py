from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET
        ), "нет кнопки добавить в корзину"

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET
        )
        button_add_to_basket.click()

    def test_price_in_basket(self):
        price_book = self.browser.find_element(
            *ProductPageLocators.OBJ_PRICE_BOOK
        ).text
        price_in_basket = self.browser.find_element(
            *ProductPageLocators.OBJ_PRICE_IN_BASKET
        ).text
        assert (
            price_book == price_in_basket
        ), "цены разные"

    def added_in_basket(self):
        text_first_alertinner = self.browser.find_element(
            *ProductPageLocators.OBJ_TEXT_ALERT_FIRST
        ).text
        name_book = self.browser.find_element(
            *ProductPageLocators.OBJ_NAME_BOOK
        ).text
        assert (
            name_book == text_first_alertinner
        ), "название книги и добавленной книги, разные"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Сообщение о успешном добовление есть, а не должно быть"

    def wait_to_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Сообщение о успешном добовление не исчезло"