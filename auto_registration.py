from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CLASS_NAME, 'form-control.first')
    first_name.send_keys('Antuan')
    last_name = browser.find_element(By.CLASS_NAME, 'form-control.second')
    last_name.send_keys('Sebastian')
    email= browser.find_element(By.CLASS_NAME,'form-control.third')
    email.send_keys('123@mail.me')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
