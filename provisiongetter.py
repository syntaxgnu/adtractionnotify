''' Get provision from Adtraction '''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME=<username_here>
PASSWORD=<password_here>

class ProvisionGetter():

headless_option = webdriver.ChromeOptions()
headless_option.add_argument('headless')

driver = webdriver.Chrome(options=headless_option)

driver.get('https://adtraction.com/sv/login')
driver.find_element_by_css_selector('form#login input[id="username"]').send_keys(USERNAME)
driver.find_element_by_css_selector('form#login input[id="password"]').send_keys(PASSWORD)
driver.find_element_by_id('loginbutton').click()

provision = ''
while(provision == ''):
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-stats"]/div/div[2]/div/span'))
        )
    provision = element.text
    time.sleep(1)

print(provision)

driver.quit()
