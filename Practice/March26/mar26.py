from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/


driver = webdriver.Chrome()
driver.get("https://www.scrapethissite.com/")

button=driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[2]/a")
button.click()

for element in driver.find_elements(By.CLASS_NAME, "page"):
    print(element.find_element(By.CSS_SELECTOR,"h3.page-title").text)
    print(element.find_element(By.CSS_SELECTOR,"p.lead.session-desc").text,"\n")

time.sleep(5)
driver.quit
