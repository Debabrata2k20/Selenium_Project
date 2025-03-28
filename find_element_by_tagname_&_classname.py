import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ByTagnameClassname():
    def element_by_tagname_and_classname(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element(By.TAG_NAME,'input').send_keys("deb@gmail.com")
        driver.find_element(By.CLASS_NAME, 'email-login-box').send_keys("deb@gmail.com")
        time.sleep(3)
Tagname_Classname = ByTagnameClassname()
Tagname_Classname.element_by_tagname_and_classname()