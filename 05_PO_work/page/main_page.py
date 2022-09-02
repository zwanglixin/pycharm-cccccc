
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from base_page import BasePage
from add_member_page import AddMember
from contact_page import Contact
import time
from selenium.webdriver.support import expected_conditions as EC
# from import_contact_page import ImportContact
# from customer_relation_page import CustomerRelation
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        first = self.find(By.CLASS_NAME, 'index_service_cnt_itemWrap')
        print("哈哈哈哈哈哈哈哈哈哈或或或或或或或或或：", first.text)
        first.click()
        self.driver.implicitly_wait(10)
        email = self.find(By.CLASS_NAME, "memberAdd_biz_mail_suffix").text
        print("1111111111111111111111111111", email)
        return AddMember(self.driver)

    def goto_contact(self):
        # self.find(By.XPATH,"//*[@id=\"menu_contacts\"]/span").click()
        # time.sleep(3)
        return Contact(self.driver)

    # def goto_import_contact(self):
    #     return ImportContact(self.driver)
    #
    # def goto_customer_relation(self):
    #     return CustomerRelation(self.driver)