from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "YOUR_PATH_HERE"
driver = webdriver.Chrome(PATH)

driver.get("https://au.indeed.com")

search = driver.find_element_by_id("text-input-what")
search.send_keys("Web Developer")
searchLoc = driver.find_element_by_id("text-input-where")
searchLoc.send_keys("Sydney")
search.send_keys(Keys.RETURN)




