#python c:\Users\BeeHoney\environments\selenium_course\test_abs_project_unittest_lesson1_6_step11.py
#pytest c:\Users\BeeHoney\environments\selenium_course\test_abs_project_unittest_lesson1_6_step11.py

import unittest
from selenium import webdriver
import time

class Test_link(unittest.TestCase):
    def test_link1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block>div:nth-child(1)>input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block>div:nth-child(2)>input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block>div:nth-child(3)>input")
        input3.send_keys("ivpet@mail.ru")
        time.sleep(3)
        button = browser.find_element_by_css_selector("button.btn").click()

        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "NoSuchElementException")
        browser.close()

    def test_link2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        time.sleep(3)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block>div:nth-child(1)>input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block>div:nth-child(2)>input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block>div:nth-child(3)>input")
        input3.send_keys("ivpet@mail.ru")
        time.sleep(3)
        button = browser.find_element_by_css_selector("button.btn").click()

        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "NoSuchElementException")

if __name__ == "__main__":
    unittest.main()

    # закрываем браузер после всех манипуляций
    browser.quit()
#
# from selenium import webdriver
# import time
# import unittest
#
# def link_t(link):
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_xpath(".//*[@placeholder = 'Введите имя']").send_keys("Иван")
#     browser.find_element_by_xpath(".//*[@placeholder = 'Введите фамилию']").send_keys("Иванов")
#     browser.find_element_by_xpath(".//*[@placeholder = 'Введите Email']").send_keys("ivan@yandex.ru")
#     browser.find_element_by_css_selector("button.btn").click()
#
#     time.sleep(1)
#     return browser.find_element_by_tag_name("h1").text
#
#
# class TestReg(unittest.TestCase):
#     def test_reg1(self):
#         self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
#                          "Поздравляем! Вы успешно зарегистировались!", "registration is failed")
#
#
#     def test_reg2(self):
#         self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
#                          "Поздравляем! Вы успешно зарегистировались!", "registration is failed")
#
# if __name__ == "__main__":
#     unittest.main()