from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from datetime import datetime

WEB_URL = "https://qa-test-todo-fa6994894c02.herokuapp.com/"
REPORT_DIR = "report"


def write_to_file(fileName: str, text: str, identifier: str = "DEBUG"):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
    filePath = os.path.join(REPORT_DIR, fileName)
    with open(filePath, 'a') as file:
        current_time = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
        textFormatted = f"{current_time} - {identifier} -- {text}" if identifier != "INFO" else text
        file.write(textFormatted + '\n')


class BaseTestCase(BaseCase):
    def __init__(self, testName, *args, **kwargs):
        super().__init__(testName, *args, **kwargs)
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.reportFile = f"test_report_{current_timestamp}.txt"
        self.testName = testName

    def setUp(self):
        super().setUp()
        write_to_file(self.reportFile,
                      f"==========================================================================================\n"
                      f"Starting {self.testName} Test"
                      f"\n---------------------------------------------------\n",
                      "INFO"
                      )

    def tearDown(self):
        write_to_file(self.reportFile,
                      f"Ending {self.testName} Test"
                      f"\n==========================================================================================\n",
                      "TEST COMPLETION"
                      )
        self.save_teardown_screenshot()
        super().tearDown()


class HelperBase(BaseTestCase):

    def open_webapp(self):
        try:
            self.maximize_window()
            time.sleep(2)
            write_to_file(self.reportFile, "Opening Web app")
            self.open(WEB_URL)
            self.assert_title("TodoMVC: React")
            time.sleep(1)
        except NoSuchElementException as e:
            write_to_file(self.reportFile, f"Element not found: {e}", "ERROR")
            self.fail(f"Test failed due to element not found: {e}")
        except Exception as e:
            write_to_file(self.reportFile, f"Test failed due to unexpected error: {e}", "ERROR")
            self.fail(f"Test failed due to unexpected error: {e}")

    def add_a_new_to_do_item(self, item: str):
        try:
            write_to_file(self.reportFile, f"Adding Item: {item} - To do list")
            self.type("#todo-input", item, timeout=5)
            time.sleep(1)
            self.find_element("#todo-input").send_keys(Keys.ENTER)
            time.sleep(2)
            if self.find_text(item, timeout=3):
                write_to_file(self.reportFile, f"Item {item} Added successfully!")
            else:
                write_to_file(self.reportFile, "Item was not added, Please investigate", "ERROR")
                self.fail("Item was not added, Please investigate")
            write_to_file(self.reportFile, "Making sure the element does not exist in the completed items")
            self.click('a:contains("Completed")', timeout=3)
            time.sleep(3)
            if self.is_element_visible(item):
                write_to_file(self.reportFile, "Element should not exist on the 'Completed' tab", "WARN")
                self.fail("Element should not exist on the 'Completed' tab")
            else:
                write_to_file(self.reportFile, "Element exist in the right place")
            self.click('a:contains("All")', timeout=3)
            time.sleep(2)
        except NoSuchElementException as e:
            write_to_file(self.reportFile, f"Element not found: {e}", "ERROR")
            self.fail(f"Test failed due to element not found: {e}")
        except Exception as e:
            write_to_file(self.reportFile, f"Test failed due to unexpected error: {e}", "ERROR")
            self.fail(f"Test failed due to unexpected error: {e}")

    def mark_to_do_item_as_completed(self, item: str):
        try:
            write_to_file(self.reportFile, f"Marking Item: -{item}- as Completed")
            self.assert_element(f"//label[text()='{item}']")
            x_offset = 15
            y_offset = 15
            label_xpath = f"//label[text()='{item}']"
            time.sleep(3)
            self.scroll_to(label_xpath)
            self.click_with_offset(label_xpath, x_offset, y_offset)
            time.sleep(3)
        except NoSuchElementException as e:
            write_to_file(self.reportFile, f"Element not found: {e}", "ERROR")
            self.fail(f"Test failed due to element not found: {e}")
        except Exception as e:
            write_to_file(self.reportFile, f"Test failed due to unexpected error: {e}", "ERROR")
            self.fail(f"Test failed due to unexpected error: {e}")

    def delete_to_do_item(self, item: str):
        try:
            write_to_file(self.reportFile, f"Deleting Item: - {item}")
            label_xpath = f"//label[text()='{item}']"
            self.assert_element(f"//label[text()='{item}']")
            elt_size = self.find_element(label_xpath, timeout=10).size
            width, height = elt_size['width'], elt_size['height']
            x_offset = width - 15
            y_offset = height - 15
            time.sleep(3)
            self.scroll_to(label_xpath)
            self.click_with_offset(label_xpath, x_offset, y_offset)
            time.sleep(3)
        except NoSuchElementException as e:
            write_to_file(self.reportFile, f"Element not found: {e}", "ERROR")
            self.fail(f"Test failed due to element not found: {e}")
        except Exception as e:
            write_to_file(self.reportFile, f"Test failed due to unexpected error: {e}", "ERROR")
            self.fail(f"Test failed due to unexpected error: {e}")
