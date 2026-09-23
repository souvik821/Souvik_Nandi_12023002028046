import time
from typing import List, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from utils.config_reader import ConfigReader


class BasePage:
    """Base Page Object encapsulating common WebDriver interactions with dynamic explicit waits."""

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout
        self.config = ConfigReader()
        self.action_delay = self.config.action_delay

    def navigate_to(self, url: str) -> None:
        """Navigates browser to target URL."""
        self.driver.get(url)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """Waits dynamically for element visibility and returns WebElement."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Waits dynamically for presence of all elements matching locator."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def click(self, locator: Tuple[str, str]) -> None:
        """Waits until element is clickable and executes click action with controlled speed."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if self.action_delay > 0:
            time.sleep(self.action_delay)
        element.click()

    def send_keys(self, locator: Tuple[str, str], text: str, clear_first: bool = True) -> None:
        """Clears input and types text sequence with controlled speed."""
        element = self.find(locator)
        if clear_first:
            element.clear()
        if self.action_delay > 0:
            time.sleep(self.action_delay)
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Extracts trimmed inner text from visible element."""
        return self.find(locator).text.strip()

    def get_title(self) -> str:
        """Returns active page title."""
        return self.driver.title.strip()

    def get_current_url(self) -> str:
        """Returns active page URL."""
        return self.driver.current_url

    def is_visible(self, locator: Tuple[str, str], timeout: int = None) -> bool:
        """Checks if element is visible within specified timeout."""
        wait_engine = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait_engine.until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_title_contains(self, text: str) -> bool:
        """Waits until page title contains expected substring."""
        try:
            return self.wait.until(EC.title_contains(text))
        except TimeoutException:
            return False
