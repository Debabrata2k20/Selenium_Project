import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GetAttributeValue():
    def get_attribute_value(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)
        driver.get("https://www.yatra.com")
        attr_value=driver.find_element(By.XPATH, "//button[normalize-space()='Search']").get_attribute("Search")
        print(attr_value)
        time.sleep(3)
Attributevalue= GetAttributeValue()
Attributevalue.get_attribute_value()

