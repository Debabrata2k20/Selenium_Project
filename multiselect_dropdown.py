import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

class MultiSelectDropdown():
    def multi_select_dropdown(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://practice.expandtesting.com/dropdown")
        time.sleep(2)
        dropdown = driver.find_element(By.ID, "country")
        dd_multi = Select(dropdown)
        #dropdown.click()
        dd_multi.select_by_visible_text("India")
        time.sleep(2)
        dd_multi.select_by_value("IT")
        time.sleep(2)
        #dd_multi.deselect_by_value("IT")
        #dd_multi.deselect_all()
DropDown = MultiSelectDropdown()
DropDown.multi_select_dropdown()