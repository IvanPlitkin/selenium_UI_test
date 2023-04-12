from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

browser = webdriver.Chrome()
browser.implicitly_wait(2)
try:
    class testFormControl(unittest.TestCase):
        def test_welcome_text(self):
                browser.get("http://suninjuly.github.io/registration1.html")
                browser.find_element(By.CLASS_NAME,'first_block > .first_class >.first').send_keys('Имя')
                browser.find_element(By.CLASS_NAME,'first_block >.second_class >.second').send_keys('Фамилия')
                browser.find_element(By.CLASS_NAME,'third_class > .third').send_keys('123@mail.me')
                browser.find_element(By.CSS_SELECTOR, "button.btn").click()                
                
                welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
                welcome_text = welcome_text_elt.text
                self.assertEqual('Congratulations! You have successfully registered!', "Congratulations! You have successfully registered!")
        
        def test_welcome_text2(self):
                browser.get("http://suninjuly.github.io/registration2.html")
                browser.find_element(By.CLASS_NAME,'first_block > .first_class >.first').send_keys('Имя')
                browser.find_element(By.CLASS_NAME,'first_block >.second_class >.second').send_keys('Фамилия')
                browser.find_element(By.CLASS_NAME,'third_class > .third').send_keys('123@mail.me')
                browser.find_element(By.CSS_SELECTOR, "button.btn").click()                   
                
                welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
                welcome_text = welcome_text_elt.text
                self.assertEqual('Congratulations! You have successfully registered!', "Congratulations! You have successfully registered!")


    if __name__ == "__main__":
        unittest.main()
finally:    
    browser.quit()
