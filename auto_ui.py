import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(executable_path= "C:\Chromedriver\chromedriver.exe")

def code_status():
    res= requests.get('http://u920152e.beget.tech/#')
    if res.status_code == 403:
        print("YES")
    else:
        print("NO")

for i in range (3):
    driver.get("http://u920152e.beget.tech/#")
    code_status() 
    driver.find_element(By.CSS_SELECTOR, '[name="auth_email"]').send_keys('abc@mail.ru')
    driver.find_element(By.CSS_SELECTOR, '[name="auth_pass"]').send_keys('123')
    driver.find_element(By.CSS_SELECTOR, '[name="form_auth_submit"]').click()
    driver.find_element(By.CSS_SELECTOR, '[value="18"]').click()
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep (3)

driver.close()