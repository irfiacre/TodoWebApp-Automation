from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)
WEB_URL = "https://qa-test-todo-fa6994894c02.herokuapp.com/"


class HtmlInspectorTests(BaseCase):
    def test_html_inspector(self):
        print("---------")
        self.open(WEB_URL)
        inspection_result = self.inspect_html()
        print("Inspection Result:\n\n", inspection_result)
