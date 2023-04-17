from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link1="http://suninjuly.github.io/registration1.html"
link2="http://suninjuly.github.io/registration2.html"

driver.implicitly_wait(2)

class testFormControl(unittest.TestCase):
    def test_welcome_text(self):
            driver.get(link1)
            driver.find_element(By.CLASS_NAME,'first_block > .first_class >.first').send_keys('Имя')
            driver.find_element(By.CLASS_NAME,'first_block >.second_class >.second').send_keys('Фамилия')
            driver.find_element(By.CLASS_NAME,'third_class > .third').send_keys('123@mail.me')
            driver.find_element(By.CSS_SELECTOR, "button.btn").click()                
            
            driver.find_element(By.TAG_NAME, "h1").text
            self.assertEqual('Congratulations! You have successfully registered!', "Congratulations! You have successfully registered!")
    
    def test_welcome_text2(self):
            driver.get(link2)
            driver.find_element(By.CLASS_NAME,'first_block > .first_class >.first').send_keys('Имя')
            driver.find_element(By.CLASS_NAME,'first_block >.second_class >.second').send_keys('Фамилия')
            driver.find_element(By.CLASS_NAME,'third_class > .third').send_keys('123@mail.me')
            driver.find_element(By.CSS_SELECTOR, "button.btn").click()                   
            
            driver.find_element(By.TAG_NAME, "h1").text
            self.assertEqual('Congratulations! You have successfully registered!', "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()


driver.quit()
