from webbrowser import BaseBrowser
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(executable_path= "C:\Chromedriver\chromedriver.exe")

driver.get("https://spb.hh.ru/")

time.sleep(2)

#кнопка войти
enterbutton= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div/div/div/div/div[5]/a')
enterbutton.click()

time.sleep(1)

driver.get ("https://spb.hh.ru/account/login?backurl=%2F&hhtmFrom=main")

#ввести mail
mailboxname= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[1]/fieldset/input')
mailboxname.send_keys('*****@m.ru')

#нажать войти с паролем
enterwithbutton2= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[5]/button[2]')
enterwithbutton2.click()

#ввести пароль
passwordbutton= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[2]/fieldset/input')
passwordbutton.send_keys('******')

#нажать войти
enterbutton2= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[5]/div/button[1]')
enterbutton2.click()


time.sleep(2)

#мои резюме
my_cv= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[1]/div/div/div/div[1]/a')
my_cv.click()


#Кнопка поиска
searchbutton= driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div[1]/div[4]/div[1]/div/div[6]/div/div[2]/a')
searchbutton.click()

time.sleep(360)

driver.close()