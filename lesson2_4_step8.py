from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    ).click()
   

    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    inp = browser.find_element_by_id('answer')
    inp.send_keys(result)

    sbmt = browser.find_element_by_tag_name('button')
    sbmt.click()


finally:
    time.sleep(5)
    browser.quit()
