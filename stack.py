from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


cred={'email':'biomorf@bigmir.net',
      'password':'5441325t'
}

class Stackoverflow:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def login(self):
        self.driver.get('https://stackoverflow.com/')
        self.driver.find_element_by_xpath('/html/body/header/div/div[2]/div/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(cred['email'])
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(cred['password'])
        self.driver.find_element_by_xpath('//*[@id="submit-button"]').click()
        time.sleep(1)

    def search(self):
        assert (self.driver.current_url.split('?')[0] != 'https://stackoverflow.com/users/login')
        self.driver.find_element_by_xpath('//*[@id="search"]/input').send_keys('python')
        self.driver.find_element_by_xpath('//*[@id="search"]/input').send_keys(Keys.ENTER)
        links = self.driver.find_elements_by_class_name('question-hyperlink')
        links[0].click()



a= Stackoverflow()
a.login()
a.search()


