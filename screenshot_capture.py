import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ScreenshotCapture():
    def screenshot_capture(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continuedemo = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test.png")
        continuedemo.click()
        time.sleep(2)
        driver.get_screenshot_as_file("D:\\Selenium_Project\\error.png")
        driver.save_screenshot(".\\test1.png")

DropDown = ScreenshotCapture()
DropDown.screenshot_capture()