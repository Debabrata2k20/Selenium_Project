import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AutoSuggestion():
    def auto_suggestion(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://flight.yatra.com/air-search-ui/dom2/trigger?ADT=1&CHD=0&INF=0&class=Economy&destination=BOM&destinationCountry=IN&flight_depart_date=11%2F03%2F2025&hb=0&noOfSegments=1&origin=DEL&originCountry=IN&type=O&unique=204849770839&viewName=normal")
        depart_from = driver.find_element(By.ID, "origin_0")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("Bhubaneswar")
        time.sleep(2)
        #depart_from.send_keys(keys.ENTER)
        going_to = driver.find_element(By.ID, "destination_0")
        going_to.send_keys("Hyderabad")
        time.sleep(2)
        search_results = driver.find_elements(By.NAME,"destination_0")
        #search_results

DropDown = AutoSuggestion()
DropDown.auto_suggestion()


