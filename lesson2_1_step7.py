from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    result = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(result)

    checkbox = browser.find_element_by_id('robotCheckbox') 
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    subbmit = browser.find_element_by_tag_name('button')
    subbmit.click()

finally:
    time.sleep(6)
    browser.quit()
