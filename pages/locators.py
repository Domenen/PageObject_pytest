from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    OBJ_NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    OBJ_PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    OBJ_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    OBJ_TEXT_ALERT_FIRST = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")