import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CheckBox():
    def check_box(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://designsystem.digital.gov/components/checkbox/")
        driver.find_element(By.XPATH, "//label[@for='check-historical-douglass-2']").click()
        time.sleep(2)
        var1 = driver.find_element(By.XPATH, "//label[@for='check-historical-douglass-2']").is_selected()
        print(var1)
        var2 = driver.find_element(By.XPATH, "//label[@for='check-historical-washington-2']").click()
        print(var2)
        time.sleep(2)

Handle_CheckBox = CheckBox()
Handle_CheckBox.check_box()