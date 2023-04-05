import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path= "C:\Chromedriver\chromedriver.exe")

def code_status():
    res= requests.post('https://piter-online.net/')
    if res.status_code == 201:
        print("YES")
    else:
        print("NO")

for i in range (5):
    driver.get("https://piter-online.net/")
    time.sleep(1)
    street_area= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/input')
    street_area.send_keys('Тестовая линия')
    time.sleep(1)
    street_area.send_keys(Keys.ENTER)
    home_area= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/input')
    home_area.send_keys('1')
    time.sleep(1)
    home_area.send_keys(Keys.ENTER)
    type_list= driver.find_element(By.CSS_SELECTOR, '.app184')
    type_list.click()
    time.sleep(1)
    type_flat=driver.find_element(By.CSS_SELECTOR, 'app184 > app186') #не работает
    type_flat.click() 
    time.sleep(1)
    find_button= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div')
    find_button.click()
    close_pop_up_button= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div')
    close_pop_up_button.click()
    connect_button= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[8]/div/div/div[2]/div[2]/a')
    connect_button.click()
    name_area= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    name_area.send_keys('Автотест')
    phone_area= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[3]/div/div[2]/input')
    phone_area.send_keys('1111111111')
    request_button= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[6]/div')
    request_button.click()
    code_status()  

time.sleep (5)

driver.close()
