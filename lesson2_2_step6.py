from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    result = calc(x)
    print(result)

    browser.execute_script('window.scrollBy(0, 100);')

    inp = browser.find_element_by_id('answer')
    inp.send_keys(str(result))

    checkbox = browser.find_element_by_id('robotCheckbox') 
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
