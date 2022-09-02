from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.remote.webdriver import WebDriver
import json
import os


class BasePage:

    base_url = ""
    def __init__(self, driver:WebDriver = None):

        if driver == None:
            self.driver = webdriver.Chrome()


        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)
            # self.driver.maximize_window()

        # 获得cookie
        cookie_file = os.path.dirname(os.path.abspath('.')) + r"\common\cookie.json"
        cookies = json.load(open(cookie_file))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.implicitly_wait(3)

    def find(self,by,value):
        return self.driver.find_element(by,value)

    def finds(self,by,value):
        return self.driver.find_elements(by,value)

    def ele_is_displayed(self,ele):
        return ele.is_displayed()

    def quit_driver(self):
        self.driver.quit()

    def sum(self,a,b):
        print("和是：",a+b)
