from typing import Tuple
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MyAccountPage(BasePage):
    """Page Object for post-authentication Account Dashboard."""

    _MY_ACCOUNT_HEADER: Tuple[str, str] = (By.XPATH, "//h2[text()='My Account']")
    _MY_ORDERS_HEADER: Tuple[str, str] = (By.XPATH, "//h2[text()='My Orders']")
    _LOGOUT_LINK: Tuple[str, str] = (By.XPATH, "//aside[@id='column-right']//a[text()='Logout']")
    _EDIT_ACCOUNT_LINK: Tuple[str, str] = (By.LINK_TEXT, "Edit your account information")

    def is_account_page_displayed(self) -> bool:
        """Validates that the user is on the My Account dashboard."""
        return self.is_visible(self._MY_ACCOUNT_HEADER, timeout=10)

    def get_header_text(self) -> str:
        return self.get_text(self._MY_ACCOUNT_HEADER)

    def click_logout(self) -> None:
        """Logs user out safely."""
        if self.is_visible(self._LOGOUT_LINK, timeout=5):
            self.click(self._LOGOUT_LINK)
