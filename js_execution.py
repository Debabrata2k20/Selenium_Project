import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class JS_Execution():
    def js_execution(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        #driver.get("https://www.mercedes-benz.com/en/")
        #driver.execute_script("window.open('https://www.mercedes-benz.com/en/')")           #URL in another window
        #driver.execute_script("window.open('https://www.mercedes-benz.com/en/', '_self')")   #particular URL in same window
        driver.execute_script("window.open('https://training.rcvacademy.com/','_self');")
        time.sleep(8)
        #element = driver.execute_script("return <p class="margin-top-10 margin-bottom-10 None dynamic-text" data-uniqid="1657512904179" style="z-index: 99999999; background-image: none; font-weight: 400; font-size: 18px; font-family: 'Open Sans'; text-align: center; font-style: normal; color: rgb(0, 0, 0); text-shadow: none; margin-top: 20px; margin-bottom: 0px; padding-top: 20px;">Curated content and learning roadmaps for people aspiring to get Software Testing/SDET Job or progress in their IT Career!</p>;")
        #driver.execute_script("arguments[0].click();",element)

Handle_JS_Execution = JS_Execution()
Handle_JS_Execution.js_execution()