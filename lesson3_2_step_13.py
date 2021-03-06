import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        # link = http://suninjuly.github.io/registration2.html
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_firstName = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input_firstName.send_keys("Ivan")
        input_lastName = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input_lastName.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input_email.send_keys("IvanPetrov@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_firstName = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input_firstName.send_keys("Ivan")
        input_lastName = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input_lastName.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input_email.send_keys("IvanPetrov@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error in test 2")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__": 
    unittest.main()