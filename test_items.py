#pytest --language=es test_items.py
#pytest --language=fr test_items.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestMainPage1():
    def test_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        but = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        try:
            assert len(but.text) != 0, "the button is missing"
        finally:
            time.sleep(10)

