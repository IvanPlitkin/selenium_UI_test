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
    mailarea= driver.find_element(By.XPATH, '/html/body/div/div/form/input[1]')
    mailarea.send_keys('abc@mail.ru')
    password= driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]')
    password.send_keys('123')
    enterbutton= driver.find_element(By.XPATH, '/html/body/div/div/form/button')
    enterbutton.click()
    radiobutton= driver.find_element(By.XPATH, '/html/body/form/ol/li[1]/input')
    radiobutton.click()
    sendbutton= driver.find_element(By.XPATH, '/html/body/form/input')
    sendbutton.click()



time.sleep (5)

driver.close()


