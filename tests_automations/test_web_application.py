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


class AutomatedTest(HelperBase):

    def test_adding_a_new_to_do_item(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_a_new_to_do_item(item)

    def test_mark_to_do_item_as_completed(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_a_new_to_do_item(item)
        time.sleep(1)
        self.mark_to_do_item_as_completed(item)

    def test_delete_to_do_item(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_a_new_to_do_item(item)
        time.sleep(1)
        self.delete_to_do_item(item)

    #
    def test_combined_tests(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_a_new_to_do_item(item)
        time.sleep(1)
        self.mark_to_do_item_as_completed(item)
        time.sleep(1)
        self.delete_to_do_item(item)


if __name__ == "__main__":
    unittest.main()
