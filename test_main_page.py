from .pages.main_page import MainPage
from .pages.login_page import LoginPage


main_link = "http://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
# pytest -v --tb=line --language=en test_main_page.py


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_page()