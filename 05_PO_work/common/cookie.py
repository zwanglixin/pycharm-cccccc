import json

import pytest
from selenium import webdriver
from time import sleep

class Test_Cookie(object):

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")


    def test_get_cookie(self):
        sleep(8) # 打开登录页面，需要手动扫码登录，然后再获取cookies
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("cookie.json","w") as f:# 把cookie写入到文件中
            json.dump(cookies, f)

    @pytest.mark.skip
    def test_cookie_login(self):
        cookies = json.loads(open("cookie.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def teardown_method(self):
        sleep(2)
        self.driver.quit()