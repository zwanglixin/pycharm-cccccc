from selenium import webdriver
import json

from selenium.webdriver.common.by import By
import time
import sys
sys.path.append(".")
from base_page import BasePage
class A(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def member(self):
        self.driver.get(self.base_url)
        first = self.find(By.CLASS_NAME, 'index_service_cnt_itemWrap')
        print("哈哈哈哈哈哈哈哈哈哈或或或或或或或或或：", first.text)
        first.click()
        time.sleep(3)
        email = self.find(By.CLASS_NAME, "memberAdd_biz_mail_suffix").text
        print("1111111111111111111111111111邮箱后缀：", email)
        self.find(By.ID, 'username').send_keys("122")
        self.find(By.ID, 'memberAdd_acctid').send_keys("1111111111111")
        self.find(By.ID, 'memberAdd_phone').send_keys("18900000002")
        self.find(By.CLASS_NAME, 'js_btn_save').click()
        self.quit_driver()
if __name__ == '__main__':
    A().member()




driver = webdriver.Chrome()
driver.find_element_by_class_name().send_keys()
# driver = webdriver.Chrome()
# driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#
# # 获得cookie
# cookie_file = "cookie.json"
# cookies = json.load(open(cookie_file))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.refresh()
# driver.implicitly_wait(3)
# member_list = []
#
# # eles = driver.find_elements(By.XPATH,"//*[@id=\"member_list\"]/tr/td")
# # for ele in eles:
# #     title = ele.get_attribute("title")
# #     # title = ele.find_element(By.XPATH, 'td').get_attribute('title')
# #     member_list.append(title)
# # print(member_list)

# driver.find_element(By.CLASS_NAME, 'index_service_cnt_itemWrap').click()
#
# time.sleep(3)
# email = driver.find_element_by_class_name("memberAdd_biz_mail_suffix").text
# print(email)
# driver.find_element(By.ID, 'username').send_keys("12345")
#
# driver.find_element(By.ID, 'memberAdd_acctid').send_keys("12345678")
# driver.find_element(By.ID, 'memberAdd_phone').send_keys("18900000000")
# driver.find_element(By.CLASS_NAME, 'js_btn_save').click()
#
# driver.quit()