import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Frames():
    def frames(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        driver.find_element(By.XPATH, "//h2[contains(text(),'HTML Examples')]").click()


DropDown = Frames()
DropDown.frames()