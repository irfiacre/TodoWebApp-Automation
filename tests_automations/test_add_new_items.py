import time
import random
import unittest
from HelperBase.base import HelperBase

TO_DO_LIST = [
    'Shopping',
    'Watching a movie',
    'Playing Basketball',
    'Scuba Diving',
    'Mountain Climbing',
    'Visit Friends',
    'Work on Project'
]
REPORT_DIR = "report"


class AutomateAddItem(HelperBase):

    def test_adding_one_item_on_to_do_list(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_a_new_to_do_item(item)
        number_of_items_xpath = f"//span[text()='1 item left!']"
        self.assert_element(number_of_items_xpath)

    def test_add_multiple_items_on_to_do_list(self):
        self.open_webapp()
        time.sleep(1)
        items_limit = random.randint(2, 5)
        for i in range(items_limit):
            item = random.choice(TO_DO_LIST)
            self.add_a_new_to_do_item(item)
        number_of_items_xpath = f"//span[text()='{items_limit} items left!']"
        self.assert_element(number_of_items_xpath)


if __name__ == "__main__":
    unittest.main()
