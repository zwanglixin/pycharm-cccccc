
from selenium.webdriver.common.by import By
from base_page import BasePage
# from page.add_member_page import AddMember
# from contact_page import Contact

class Contact(BasePage):
    # def goto_add_member(self):
    #     self.find(By.CLASS_NAME,"qui_btn ww_btn js_add_member").click()
    #     return AddMember(self.driver)

    # 获取列表全部成员
    def get_member(self):
        member_list = []
        eles = self.finds(By.XPATH,"//*[@id=\"member_list\"]/tr/td")
        for ele in eles:
            title = ele.get_attribute('title')
            member_list.append(title)
        print(member_list)
        return member_list
