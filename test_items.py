#pytest --language=es test_items.py
#pytest --language=fr test_items.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    but = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(but) != 0, "the button is missing"
