# -*- coding=utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.common import exceptions
from bs4 import BeautifulSoup
import time


class Driver(object):
    driver = None

    #def __init__(self):
    #    self.driver = None

    #@staticmethod
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "OnePlus3"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        try:
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        except exceptions.WebDriverException:
            print('Err driver')

        self.driver.implicitly_wait(20)
        time.sleep(6)
        #Driver.driver = driver

    #@staticmethod
    def get_curr_driver(self):
        print("Fuck----") #,sDriver.driver
        return self.driver

    def stop(self):
        self.driver.quit()

# Driver.start()
# fd = Driver.get_curr_driver()
# bs = BeautifulSoup(fd.page_source,"html.parser")
# print bs.prettify()
#
# fd.find_element(By.ID, "home_search").click()
