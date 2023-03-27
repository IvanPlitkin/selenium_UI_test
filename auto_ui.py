import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(executable_path= "C:\Chromedriver\chromedriver.exe")

driver.get("http://u920152e.beget.tech/#")

time.sleep(2)

# Имейл
mailarea= driver.find_element(By.XPATH, '/html/body/div/div/form/input[1]')
mailarea.send_keys('abc@mail.ru')

# Пароль
password= driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]')
password.send_keys('123')

time.sleep (2)

# Войти
enterbutton= driver.find_element(By.XPATH, '/html/body/div/div/form/button')
enterbutton.click()

# Младше 18
radiobutton= driver.find_element(By.XPATH, '/html/body/form/ol/li[1]/input')
radiobutton.click()

# Отправить 
sendbutton= driver.find_element(By.XPATH, '/html/body/form/input')
sendbutton.click()

time.sleep (5)

driver.close()