from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyttsx3 as p
import speech_recognition as sr
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



sr.Microphone(device_index=1)

r = sr.Recognizer()
engine=p.init()
engine.setProperty('rate', 165)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def send_msg():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 500)
    c=0
    while c!=1:
        with sr.Microphone() as source:
            engine.say("Who do you want to send the message to?")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source)
            contact_name = r.listen(source)
            try:
                contact_name_char = r.recognize_google(contact_name)
                c=1
            except sr.UnknownValueError:
                engine.say("Could you please repeat yourself")
            except sr.RequestError as e:
                engine.say("Error")
    target = '"contact_name_char"'
    # Replace the below string with your own message
    d=0
    while d!=1:
        with sr.Microphone() as source:
            engine.say("Who is the message content?")
            engine.runAndWait()
            msg_content = r.listen(source)
            try:
                msg_content_char = r.recognize_google(msg_content)
                d=1
            except sr.UnknownValueError:
                engine.say("Could you please repeat yourself")
            except sr.RequestError as e:
                engine.say("Error")
    string = '"msg_content_char"'
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
