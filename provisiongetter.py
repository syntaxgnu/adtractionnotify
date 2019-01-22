''' Get provision from Adtraction '''
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'

class ProvisionGetter():
    ''' Class that gets yesterdays provision and sends
        a notification to the user '''
    def __init__(self):
        headless_option = webdriver.ChromeOptions()
        headless_option.add_argument('headless')

        self.driver = webdriver.Chrome(options=headless_option)

        self.logging = logging.getLogger('ProvisionGetter')
        self.logging.setLevel(level=logging.DEBUG)

    def get_provision(self):
        ''' Get provision and return it '''
        provision = ''
        self.driver.get('https://adtraction.com/sv/login')
        self.driver.find_element_by_css_selector('form#login input[id="username"]')\
                                                 .send_keys(USERNAME)
        self.driver.find_element_by_css_selector('form#login input[id="password"]')\
                                                 .send_keys(PASSWORD)
        self.driver.find_element_by_id('loginbutton').click()
        self.logging.debug('Clicked login button')

        while provision == '':
            self.logging.debug('Waiting for element')
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="main-stats"]/div/div[2]/div/span'))
            )
            provision = element.text
            if provision == '':
                self.logging.debug('element hasn\'t showed up yet')
                time.sleep(1)
            else:
                self.logging.debug('Got provision: %s', str(provision))

        return provision

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        ''' Handle cleanup of driver '''
        self.driver.quit()
