from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
# pytest -v --tb=line --language=en test_main_page.py


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()