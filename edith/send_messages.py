from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def send_msg(x,y):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 500)
    target = '"x"'
    # Replace the below string with your own message
    string = '"y"'
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@dir = "ltr"][@spellcheck = "true"][@contenteditable = "true"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    for i in range(1):
        input_box.send_keys(string + Keys.ENTER)
        time.sleep(1)
