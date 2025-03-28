import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ElementsList():
    def locate_elements_list(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        list = driver.find_elements(By.TAG_NAME,'a')
        print(len(list))
        for i in list:
            print(i.text)
        time.sleep(3)
ListElement = ElementsList()
ListElement.locate_elements_list()