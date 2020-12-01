from selenium import webdriver
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    next_window = browser.window_handles[1]
    browser.switch_to.window(next_window)

    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    inp = browser.find_element_by_id('answer')
    inp.send_keys(result)

    sbmt = browser.find_element_by_tag_name('button')
    sbmt.click()


finally:
    time.sleep(5)
    browser.quit()
