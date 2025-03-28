import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ByLinkText():
    def locate_by_linktext(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://www.yatra.com/")
        driver.find_element(By.PARTIAL_LINK_TEXT,'Yatra for Business').click()
        time.sleep(3)
Linktext = ByLinkText()
Linktext.locate_by_linktext()
