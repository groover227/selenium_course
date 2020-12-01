from selenium import webdriver
import time
import os 

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Max')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Max')

    email = browser.find_element_by_name('email')
    email.send_keys('Max@max.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_input = browser.find_element_by_id('file')
    file_input.send_keys(file_path)

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
