from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://metanit.com/')

time.sleep(1)

el = driver.find_elements(By.LINK_TEXT, "Python")
el[0].click()

time.sleep(1)

el = driver.find_elements(By.LINK_TEXT, "Руководство по Python")
el[0].click()

time.sleep(10)