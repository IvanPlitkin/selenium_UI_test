from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'form-control.first').send_keys('Имя')
    browser.find_element(By.CLASS_NAME, 'form-control.second').send_keys('Фамилия')
    browser.find_element(By.CLASS_NAME,'form-control.third').send_keys('123@mail.me')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()                
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
