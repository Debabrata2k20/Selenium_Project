import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

class Sliders():
    def sliders(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.snapdeal.com/search?keyword=mobile%20phone&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
        driver.maximize_window()
        elem1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        elem2 = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        # for elem1
        ActionChains(driver).drag_and_drop_by_offset(elem1, 60 ,0).perform()
        #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50,0).release().perform()
        #ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80,0).release().perform()
        time.sleep(2)
        # for elem2
        #ActionChains(driver).drag_and_drop_by_offset(elem2, -60 ,0).perform()
        #ActionChains(driver).click_and_hold(elem2).pause(1).move_by_offset(-50,0).release().perform()
        ActionChains(driver).move_to_element(elem2).pause(1).click_and_hold(elem2).move_by_offset(-80,0).release().perform()
        
Handle_Sliders = Sliders()
Handle_Sliders.sliders()