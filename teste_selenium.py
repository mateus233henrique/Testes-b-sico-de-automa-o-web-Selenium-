import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com/')

username = browser.find_element(By.ID,'user-name').send_keys('standard_user')
password = browser.find_element(By.ID,'password').send_keys('secret_sauce')
login = browser.find_element(By.ID,'login-button').click()

time.sleep(3)

print("finished...")