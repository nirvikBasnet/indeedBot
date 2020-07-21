from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://au.indeed.com")

search = driver.find_element_by_id("text-input-what")
search.send_keys("cleaner")
searchLoc = driver.find_element_by_id("text-input-where")
searchLoc.send_keys("sydney")
search.send_keys(Keys.RETURN)


try:
    resultsCol = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "resultsCol"))
    )

    
    

except:
    driver.quit()


