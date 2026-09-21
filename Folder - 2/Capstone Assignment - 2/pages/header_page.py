from typing import Tuple
from selenium.webdriver.common.by import By
from .base_page import BasePage


class HeaderPage(BasePage):
    """Reusable navigation header component across all pages."""

    _MY_ACCOUNT_DROPDOWN: Tuple[str, str] = (By.CSS_SELECTOR, "a[title='My Account']")
    _LOGIN_LINK: Tuple[str, str] = (By.LINK_TEXT, "Login")
    _REGISTER_LINK: Tuple[str, str] = (By.LINK_TEXT, "Register")
    _LOGOUT_LINK: Tuple[str, str] = (By.LINK_TEXT, "Logout")
    _SEARCH_INPUT: Tuple[str, str] = (By.NAME, "search")
    _SEARCH_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "#search button")

    def navigate_to_login(self) -> None:
        self.click(self._MY_ACCOUNT_DROPDOWN)
        self.click(self._LOGIN_LINK)

    def navigate_to_register(self) -> None:
        self.click(self._MY_ACCOUNT_DROPDOWN)
        self.click(self._REGISTER_LINK)

    def quick_search(self, term: str) -> None:
        self.send_keys(self._SEARCH_INPUT, term)
        self.click(self._SEARCH_BUTTON)
