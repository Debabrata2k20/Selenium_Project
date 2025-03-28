import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


class Drag_Drop():
    def drag_drop(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.XPATH,"//div[@id='draggable']")
        elem2 = driver.find_element(By.ID,"droppable")
        #ActionChains(driver).drag_and_drop(elem1,elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1,100,100).perform()
        time.sleep(4)

Handle_Drag_Drop = Drag_Drop()
Handle_Drag_Drop.drag_drop()