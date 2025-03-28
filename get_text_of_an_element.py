import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GetElementText():
    def get_text_element(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        text=driver.find_element(By.XPATH, "//p[contains(text(),'Tirupati Darshan: 10 Interesting Facts You Must Kn')]").text
        print(text)
        time.sleep(3)
TextElement = GetElementText()
TextElement.get_text_element()