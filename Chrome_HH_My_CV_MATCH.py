from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
driver= webdriver.Chrome()     

try:
    driver.get("https://spb.hh.ru/")
    driver.find_element(By.CSS_SELECTOR, '[data-qa="login"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-qa="account-signup-email"]').send_keys('testn@email.ru')
    driver.find_element(By.CSS_SELECTOR, '[data-qa="expand-login-by-password"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-qa="login-input-password"]').send_keys('123')
    driver.find_element(By.CSS_SELECTOR, '[data-qa="account-login-submit"]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="mainmenu_myResumes"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-qa="resume-recommendations__button_editResume"]').click()
    

finally:

    time.sleep(30)

    driver.close()
