#pytest -s -v c:\Users\BeeHoney\environments\selenium_course\test_3_6_3.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

# answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():
    @pytest.mark.parametrize('links',
                             ["https://stepik.org/lesson/236895/step/1",
                              "https://stepik.org/lesson/236896/step/1",
                              "https://stepik.org/lesson/236897/step/1",
                              "https://stepik.org/lesson/236898/step/1",
                              "https://stepik.org/lesson/236899/step/1",
                              "https://stepik.org/lesson/236903/step/1",
                              "https://stepik.org/lesson/236904/step/1",
                              "https://stepik.org/lesson/236905/step/1"]
                             )
    def test_link(self, browser, links):
        #self = ''
        answer = ''
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(10)

        input = browser.find_element_by_tag_name("textarea")
        input.send_keys(str(math.log(int(time.time()))))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
        message = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text

        try:
            assert "Correct!" == message
        except AssertionError:
            answer += message  # собираем ответ с каждой ошибкой
        print(answer)