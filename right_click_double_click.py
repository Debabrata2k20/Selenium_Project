import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

class RightclickDoubleclick():
    def Rightclick_Doubleclick(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        #Right click
        # click = ActionChains(driver)
        # right_click = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        # copy_element = driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        # click.context_click(right_click).perform()
        # time.sleep(2)
        # copy_element.click()
        # time.sleep(3)

        #Double click
        click = ActionChains(driver)
        double_click = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        click.double_click(double_click).perform()
        time.sleep(3)

Handle_RightclickDoubleclick = RightclickDoubleclick()
Handle_RightclickDoubleclick.Rightclick_Doubleclick()