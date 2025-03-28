import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ByXpath():
    def locate_by_xpath(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH,'//input[@id="login-input"]').send_keys("deb@gmail.com")
        time.sleep(3)
By_XPATH = ByXpath()
By_XPATH.locate_by_xpath()


