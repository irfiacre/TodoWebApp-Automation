from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
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
        self.maximize_window()
        time.sleep(2)
        write_to_file(self.reportFile, "Opening Web app")
        self.open(WEB_URL)
        self.assert_title("TodoMVC: React")
        time.sleep(1)

    def add_a_new_to_do_item(self, item: str):
        write_to_file(self.reportFile, f"Adding Item: {item} - To do list")
        self.type("#todo-input", item, timeout=5)
        time.sleep(1)
        self.find_element("#todo-input").send_keys(Keys.ENTER)
        time.sleep(3)
        if self.find_text(item, timeout=3):
            write_to_file(self.reportFile, f"Item {item} Added successfully!")
        else:
            write_to_file(self.reportFile, "Item was not added, Please investigate")
        write_to_file(self.reportFile, "Making sure the element does not exist in the completed items")
        self.click('a:contains("Completed")', timeout=3)
        time.sleep(3)
        if self.is_element_visible(item):
            write_to_file(self.reportFile, "Element should not exist on the 'Completed' tab", "WARN")
            exit(0)
        else:
            write_to_file(self.reportFile, "Element exist in the right place")
        self.click('a:contains("All")', timeout=3)
        time.sleep(2)

    def edit_a_new_to_do_item(self):
        pass

    def mark_to_do_item_as_completed(self, item: str):
        write_to_file(self.reportFile, f"Marking Item: -{item}- as Completed")
        # label_elt = self.find_element(f"//label[text()='{item}']", timeout=4)
        # label_elt = self.find_element("div input", timeout=10)
        self.assert_element(f"//label[text()='{item}']")
        # todo_item_checkbox = self.find_element(
        #     f'//label[text()="{item}"]/preceding-sibling::input[@class="toggle"]',
        #     timeout=5
        # )
        # time.sleep(2)
        # self.execute_script('arguments[0].click();', todo_item_checkbox)

        # label_elt = self.find_element("div.view", timeout=10)
        # self.click("div.view")
        # time.sleep(5)
        # hidden_elt = "div.view input.toggle"
        # write_to_file(self.reportFile,"====================== =============== -----------------------")
        # self.execute_script('arguments[0].click();', self.find_element(hidden_elt))
        # self.highlight(label_elt)
        # label_elt = self.find_element("div.view input.toggle", timeout=10)
        # self.highlight(label_elt)
        # label_elt = self.find_element("div.view input.toggle", timeout=10)
        # self.highlight(label_elt)

        self.click_with_offset("div.view", 15, 15, mark=True, timeout=10, center=None)

        # self.highlight_if_visible("//input[@type='checkbox']", by="xpath")
        # time.sleep(3)
        # self.click_xpath("(//input[@type='checkbox'])")
        # self.highlight('toggle')
        x_offset = 100  # Replace with the actual x-coordinate
        y_offset = 200  # Replace with the actual y-coordinate
        # self.execute_script()
        # self.highlight("button")
        # self.click("toggle", timeout=5)
        # inspection_result = self.inspect_html()
        # write_to_file(self.reportFile,"Inspection Result:\n\n", inspection_result)
        # time.sleep(2)
        # self.assert_element("complete", timeout=5)
        time.sleep(60)

    def delete_to_do_item(self, item: str):
        write_to_file(self.reportFile, f"Marking Item: {item} as Completed")
        self.click("[data-test-id='new-item-input']", timeout=3)
        time.sleep(2)
        self.assert_element("complete", timeout=5)
