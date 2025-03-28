import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Alert():
    def alert(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        #Accept Alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        #Dismiss Alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)

        #Send text in Alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Hey Deb!")
        driver.switch_to.alert.accept()
        #Alert(driver).accept()
        time.sleep(2)

Handle_CheckBox = Alert()
Handle_CheckBox.alert()