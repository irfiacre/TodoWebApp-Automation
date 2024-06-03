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


class AutomateDeleteItem(HelperBase):

    def test_add_an_item_and_delete_it(self):
        self.open_webapp()
        time.sleep(1)
        item = random.choice(TO_DO_LIST)
        self.add_item(item)
        time.sleep(1)
        self.delete_to_do_item(item)
        time.sleep(2)

    def test_delete_multiple_items(self):
        self.open_webapp()
        time.sleep(1)
        for _ in range(random.randint(2, 4)):
            item = random.choice(TO_DO_LIST)
            self.add_item(item)
        time.sleep(1)
        self.mark_multiple_items_as_completed()
        time.sleep(1)
        self.delete_multiple_items()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
