import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import os

@pytest.fixture
def driver():
    """Фикстура для запуска и завершения браузера"""
    options = Options()
    options.add_argument("--start-maximized")
    prefs = {
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    yield driver

    # Скриншот теста
    if hasattr(driver, "get_screenshot_as_png"):
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

    driver.quit()