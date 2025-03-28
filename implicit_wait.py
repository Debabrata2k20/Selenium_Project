import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Implicit_wait():
    def implicit_wait(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.maximize_window()
        driver.find_element(By.ID,"username").send_keys("Debabrata Sahu")
        driver.find_element(By.ID,"password").send_keys("Deb@123")


Handle_Implicit_wait = Implicit_wait()
Handle_Implicit_wait.implicit_wait()