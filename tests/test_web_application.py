import logging
from seleniumbase import BaseCase, decorators
from selenium.webdriver.common.keys import Keys
import time
import random
import os

WEB_URL = "https://qa-test-todo-fa6994894c02.herokuapp.com/"
TO_DO_LIST = [
    'Shopping',
    'Watching a movie',
    'Playing Basketball',
    'Scuba Diving',
    'Mountain Climbing',
    'Visit Friends',
    'Work on Project'
]
REPORT_FILE = "report.txt"


class BaseTestCase(BaseCase):
    def setUp(self):
        super().setUp()
        print("<<< Starting Test >>>")

    def tearDown(self):
        self.save_teardown_screenshot()
        self.append_data_to_logs("Ending Test", REPORT_FILE)
        super().tearDown()
        print(">>> Stopping Test <<<")


class HomeTest(BaseTestCase):

    @decorators.rate_limited(3.5)
    def logger_info(self, text: str):
        print(f"===== INFO ======", text)

    @decorators.rate_limited(3.5)
    def logger_warning(self, text: str):
        print(f"===== WARNING ======", text)

    def open_webapp(self):
        print("Opening the webpage")
        self.open(WEB_URL)
        self.assert_title("TodoMVC: React")

    def add_a_new_to_do_item(self, item: str):
        print(f"Add Item: {item} - To do list")
        self.type("#todo-input", item, timeout=5)
        time.sleep(1)
        self.find_element("#todo-input").send_keys(Keys.ENTER)
        time.sleep(3)
        if self.find_text(item, timeout=3):
            print("Item Added successfully!")
        else:
            print("Item was not added, Please investigate")
        time.sleep(2)

    def edit_a_new_to_do_item(self):
        pass

    def mark_to_do_item_as_completed(self, item: str):
        print(f"Marking Item: {item} as Completed")
        self.find_element(f"//label[text()='{item}']", timeout=4).click()
        self.click("toggle", timeout=5)
        inspection_result = self.inspect_html()
        print("Inspection Result:\n\n", inspection_result)
        time.sleep(2)
        self.assert_element("complete", timeout=5)
        time.sleep(3)

    def delete_to_do_item(self, item: str):
        self.append_data_to_logs(f"Marking Item: {item} as Completed", REPORT_FILE)
        self.click("[data-test-id='new-item-input']", timeout=3)
        time.sleep(2)
        self.assert_element("complete", timeout=5)

    def test_webapp(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_a_new_to_do_item(item)
        self.mark_to_do_item_as_completed(item)


if __name__ == "__main__":
    import pytest

    pytest.main(["-s", __file__])
