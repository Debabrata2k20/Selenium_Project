import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class RadioButton():
    def radio_button(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://designsystem.digital.gov/components/radio-buttons/")
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//label[normalize-space()='Frederick Douglass']").is_selected())
        driver.find_element(By.XPATH, "//label[normalize-space()='Frederick Douglass']").click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//label[normalize-space()='Frederick Douglass']").is_selected())
        driver.find_element(By.XPATH, "//label[@for='historical-washington']").click()
       # print(driver.find_element(By.XPATH, "//label[normalize-space()='Frederick Douglass']").is_selected())
        print(driver.find_element(By.XPATH, "//label[@for='historical-washington']").is_selected())
        time.sleep(2)

Handle_RadioButton = RadioButton()
Handle_RadioButton.radio_button()