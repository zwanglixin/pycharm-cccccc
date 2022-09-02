from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base_page import BasePage
from contact_page import Contact
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddMember(BasePage):

    def add_member_success(self):
        time_str = str(int(time.time()))
        name = 'test' + time_str
        id = time_str
        phone = '1' + time_str
        self.sum(1,2)  # 这个方法可以调用

        name = self.find(By.ID, 'username')
        name.send_keys("99999999")
        time.sleep(10)
        # self.find(By.ID, 'memberAdd_acctid').send_keys(id)
        # self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        # self.find(By.CLASS_NAME, 'js_btn_save').click()
        return Contact(self.driver), name

    def add_member_fail(self):
        pass
