import time
import random
import unittest
from HelperBase.base import HelperBase, write_to_file

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


class AutomateMarkItemsAsRead(HelperBase):

    def test_add_item_and_mark_as_completed(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_item(item)
        time.sleep(1)
        self.mark_to_do_item_as_completed(item)
        time.sleep(2)

    def test_add_multiple_items_and_mark_as_completed(self):
        self.open_webapp()
        time.sleep(1)
        for _ in range(random.randint(2, 4)):
            item = random.choice(TO_DO_LIST)
            self.add_item(item)
        time.sleep(1)
        self.mark_multiple_items_as_completed()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
