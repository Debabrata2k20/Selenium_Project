import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HandleHiddenElement():
    def handle_hidden_element(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(element)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        element1 = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(element1)
        time.sleep(3)

Hiddenelement = HandleHiddenElement()
Hiddenelement.handle_hidden_element()