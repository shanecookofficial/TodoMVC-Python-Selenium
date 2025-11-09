from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class TodoPage(BasePage):
    # CONSTANTS
    URL = "https://todomvc.com/examples/react/dist/"

    # LOCATORS
    TODO_INPUT = (By.ID, "todo-input")
    TODO_COUNT = (By.CLASS_NAME, "todo-count")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
