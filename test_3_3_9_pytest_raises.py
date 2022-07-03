#pytest c:\Users\BeeHoney\environments\selenium_course\test_3_3_9_pytest_raises.py
#pytest c:\Users\BeeHoney\environments\selenium_course\test_3_3_9_pytest_raises.py::test_exception1
#pytest c:\Users\BeeHoney\environments\selenium_course\test_3_3_9_pytest_raises.py::test_exception2

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

if __name__ == "__main__":
    test_exception1()
    test_exception2()
    print("Everything passed")
