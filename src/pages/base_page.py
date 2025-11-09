from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    URL = ""

    def __new__(cls, *args, **kwargs):
        if cls is BasePage:
            raise TypeError("BasePage cannot be instantiated directly.")
        return super().__new__(cls)

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def goto(self):
        if not self.URL:
            raise ValueError(f"{self.__class__.__name__} has no URL defined.")
        self.driver.get(self.URL)
