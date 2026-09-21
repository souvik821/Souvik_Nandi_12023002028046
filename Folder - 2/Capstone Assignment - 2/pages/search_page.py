from typing import List, Tuple
from selenium.webdriver.common.by import By
from .base_page import BasePage


class SearchPage(BasePage):
    """Page Object for TutorialsNinja Product Search functionality."""

    # Encapsulated Locators
    _SEARCH_INPUT: Tuple[str, str] = (By.NAME, "search")
    _SEARCH_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "#search button")
    _PRODUCT_LAYOUTS: Tuple[str, str] = (By.CSS_SELECTOR, ".product-layout")
    _PRODUCT_TITLES: Tuple[str, str] = (By.CSS_SELECTOR, ".product-layout .caption h4 a")
    _NO_PRODUCT_MESSAGE: Tuple[str, str] = (By.XPATH, "//div[@id='content']//p[contains(text(),'There is no product')]")
    _SEARCH_CRITERIA_HEADER: Tuple[str, str] = (By.XPATH, "//h1[contains(text(),'Search -') or contains(text(),'Search')]")

    def open(self, base_url: str = "https://tutorialsninja.com/demo/") -> "SearchPage":
        self.navigate_to(base_url)
        return self

    def enter_search_term(self, term: str) -> "SearchPage":
        self.send_keys(self._SEARCH_INPUT, term)
        return self

    def click_search(self) -> None:
        self.click(self._SEARCH_BUTTON)

    def search_product(self, term: str) -> None:
        """Performs full search flow for specified keyword."""
        self.enter_search_term(term)
        self.click_search()

    def get_product_names(self) -> List[str]:
        """Returns list of product titles rendered in search results."""
        elements = self.find_all(self._PRODUCT_TITLES)
        return [elem.text.strip() for elem in elements if elem.text.strip()]

    def is_product_displayed(self, expected_name: str) -> bool:
        """Asserts whether specific product name exists within results."""
        titles = self.get_product_names()
        return any(expected_name.lower() in t.lower() for t in titles)

    def get_no_product_text(self) -> str:
        """Retrieves message when search yield no results."""
        return self.get_text(self._NO_PRODUCT_MESSAGE)

    def has_results(self) -> bool:
        """Returns True if at least one product layout exists."""
        return self.is_visible(self._PRODUCT_LAYOUTS, timeout=5)
