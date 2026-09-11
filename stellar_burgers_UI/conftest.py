import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.constructor_page import ConstructorPage
from url import MAIN_URL
from locators.login_locators import LoginLocators


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        pytest.fail(f"Неизвестный браузер: {browser}")

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def authorized_driver(driver):
    base = ConstructorPage(driver)  
    base.open(MAIN_URL) 
    base.click_element(LoginLocators.PERSONAL_ACCOUNT_BUTTON)
    base.send_keys_to_element(LoginLocators.EMAIL_FIELD, "teststudent@yandex.ru") 
    base.send_keys_to_element(LoginLocators.PASSWORD_FIELD, "password123456")
    base.click_element(LoginLocators.LOGIN_BUTTON)
    base._wait_for_element(LoginLocators.ORDER_BUTTON, timeout=15)
    return driver
