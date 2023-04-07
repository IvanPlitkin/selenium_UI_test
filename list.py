from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

driver=webdriver.Chrome()

def fun(x,y):
     str(x+y)

try:
    driver.get('http://suninjuly.github.io/selects1.html')
    x_element = driver.find_element(By.ID, "num1")
    x= int(x_element.text)
    y_element = driver.find_element(By.ID, "num2")
    y= int(y_element.text)
    z= fun(x,y)
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(z)
    driver.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(5)
    driver.quit()