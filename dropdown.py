import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

class Dropdown():
    def dropdown(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(2)
        drop_down = driver.find_element(By.XPATH, "//option[@value='option2']")
        drop_down.click()
DropDown = Dropdown()
DropDown.dropdown() 

