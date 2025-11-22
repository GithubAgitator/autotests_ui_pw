
class Base:
    def __init__(self, browser):
        self.browser = browser

    """Метод открытия браузера"""
    def visit(self, url: str):
        self.browser.goto(url)


    """Method GET current url"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Current url {get_url}')

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method assert url"""
    def assert_url(self, res):
        get_url = self.browser.current_url
        assert get_url == res
        print("Get value url")