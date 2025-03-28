import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ElementIsEnabledOrNot():
    def element_is_enabled_or_not(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://training.openspan.com/login")
        element_enable=driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(element_enable)
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("testingabcd")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("testingxyzz")
        time.sleep(2)
        element_enable1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(element_enable1)

EnabledOrNot = ElementIsEnabledOrNot()
EnabledOrNot.element_is_enabled_or_not()
