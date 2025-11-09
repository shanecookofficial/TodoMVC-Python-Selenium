from src.pages.todo_page import TodoPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import src.utils as utils
import random


def test_create_todo_no_todo_present(driver):
    """
    1. Navigate to https://todomvc.com/examples/react/dist/ .
    - The What needs to be done? input is visible.
    - There are no Todo's present.

    2.	Enter a string of characters into the What needs to be done? input, the press Enter.
    - The Todo item populates under the What needs to be done? input.
    - The todo-count span becomes visible, containing the phrase "1 item left!".
    """

    # 1. Navigate to https://todomvc.com/examples/react/dist/ .
    todo_page = TodoPage(driver)
    driver.get(todo_page.URL)
    todo_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(todo_page.TODO_INPUT)
    )
    todo_items = driver.find_elements(By.XPATH, "//*[@data-testid='todo-item']")
    assert len(todo_items) == 0, f"There are {len(todo_items)} todo items present."

    # 2. Enter a string of characters into the What needs to be done? input, the press Enter.
    todo_item_label = utils.generate_random_string(random.randint(3, 15))
    todo_input.send_keys(todo_item_label)
    todo_input.send_keys(Keys.ENTER)
    todo_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@data-testid='todo-item'][1]"))
    )
    assert todo_item.text == todo_item_label, (
        f"The todo item's label is '{todo_item.text}' instead of the expected '{todo_item_label}'."
    )
    todo_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(todo_page.TODO_COUNT)
    )
    assert todo_count.text == "1 item left!", (
        f"The todo count's text is '{todo_count.text}' instead of the expected '1 item left!'"
    )
