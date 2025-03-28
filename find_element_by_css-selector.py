import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ByCssSelector():
    def locate_by_css_selector(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR,'#login-input').send_keys("deb@gmail.com")
        time.sleep(3)
Cssselector = ByCssSelector()
Cssselector.locate_by_css_selector()


