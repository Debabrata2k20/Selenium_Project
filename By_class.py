import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DemoByID():
    def locate_by_id(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CLASS_NAME,'email-login-box').send_keys("deb@gmail.com")
        driver.find_element(By.ID, 'login-input').send_keys("deb@gmail.com")
        time.sleep(3)
findByID = DemoByID()
findByID.locate_by_id()