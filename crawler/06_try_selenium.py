import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)

form_xpath = '/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea'
driver.find_element(by=By.XPATH, value=form_xpath).send_keys("data engineer")

time.sleep(3)

search_button_xpath = "/html/body/div[2]/div[4]/form/div[1]/div[1]/div[2]/div[4]/div[6]/center/input[1]"
# search_button_xpath = "/html/body/div[2]/div[4]/form/div[1]/div[1]/div[2]/div[4]/div[7]/center/input[1]"
driver.find_element(by=By.XPATH, value=search_button_xpath).click()

time.sleep(20)
driver.quit()
