

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common import exceptions #.NoSuchElementException
#from appium import WebElement
from driver import Driver


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locate):
        try:
            self.driver.find_element(*locate)
        except exceptions.NoSuchElementException:
            inorge = self.driver.find_element(By.ID, "md_buttonDefaultNegative")
            if inorge :
                inorge.click()
        #element.click()
        return self.driver.find_element(*locate)

    def text(self, content):
        return (By.XPATH, "//*[@text='"+content +"']")#/[@text='行情']





class MainPage(BasePage):

    def start(self):
        pass

    def goto_search(self):
        self.find(By.ID, "home_search").click()
        return SearchPage(self.driver)



class SearchPage(BasePage):
    def search(self, keyword):
        self.find(By.ID, "search_input_text").send_keys(keyword)
        return self

    def cancel(self):
        self.find(By.ID, "action_close").click()
        return MainPage(self.driver)

    def get_all(self):
        _list = []
        stocks = self.driver.find_elements(By.ID, "stockName")
        for s in stocks :
            _list.append(s.text)
        return _list


    def add_selected(self):
        _list = []
        select = self.find(By.XPATH,"//*[contains(@resource-id, 'follow') and contains(@resource-id, '_btn')]")
        _list.append(select.get_attribute("resourceId"))
        select.click()
        select2 = self.find(By.XPATH, "//*[contains(@resource-id, 'follow') and contains(@resource-id, '_btn')]")
        _list.append(select.get_attribute("resourceId"))
        select2.click()

        return _list

    def remove_select(self):
        pass


# driver = Driver()
# driver.start()
# #driver.start()
#
# basePage = MainPage(driver.get_curr_driver())
# search = basePage.goto_search()#find(By.ID,"user_profile_icon")
# search.cancel()
# basePage.goto_search()
# search.search("mi")
# all = search.get_all()
# print(all)
#
#
# opset = search.add_selected()
#
# print(opset)
#
# search.search("alibaba")
# opset = search.add_selected()
# all = search.get_all()
# print(all)
# print(opset)
