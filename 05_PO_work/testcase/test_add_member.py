import sys
sys.path.append("..\page")
from page.main_page import MainPage

class TestAddMember(object):

    def setup(self):
        self.main = MainPage()

    def test_add_member_success(self):
        self.contact, self.name = self.main.goto_add_member().add_member_success()
        assert self.name in self.contact.get_member()

    def teardown(self):
        self.main.quit_driver()
