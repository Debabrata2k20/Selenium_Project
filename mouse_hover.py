import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

class MouseHover():
    def mouse_hover(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.yatra.com/react-home?utm_source=google&utm_medium=search&utm_campaign=brand&_gcl&utm_source=google&utm_medium=cpc&utm_campaign=&gad_source=1&gclid=Cj0KCQjw1um-BhDtARIsABjU5x713us_YEm3j05vb6nGGWv-4uHAJE-Qn_X7aRrBhLd5yqSXTfGtzXsaApzGEALw_wcB")
        driver.maximize_window()
        more_button = driver.find_element(By.XPATH,"//div[@class='MuiBackdrop-root MuiBackdrop-invisible MuiModal-backdrop css-esi9ax']")
        action = ActionChains(driver)
        action.move_to_element(more_button).perform()
        #time.sleep(2)
        driver.find_element(By.CLASS_NAME,"MuiTypography-root MuiTypography-body1 css-rrtzk2")
        time.sleep(2)
Handle_CheckBox = MouseHover()
Handle_CheckBox.mouse_hover()