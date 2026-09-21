from typing import Tuple
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object for TutorialsNinja Account Login page."""

    # Encapsulated Private Locators
    _EMAIL_INPUT: Tuple[str, str] = (By.ID, "input-email")
    _PASSWORD_INPUT: Tuple[str, str] = (By.ID, "input-password")
    _LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "input[value='Login']")
    _ALERT_DANGER: Tuple[str, str] = (By.CSS_SELECTOR, ".alert-danger")
    _FORGOTTEN_PASSWORD_LINK: Tuple[str, str] = (By.LINK_TEXT, "Forgotten Password")
    _PAGE_HEADER: Tuple[str, str] = (By.XPATH, "//h2[text()='Returning Customer']")

    def open(self, login_url: str = "https://tutorialsninja.com/demo/index.php?route=account/login") -> "LoginPage":
        """Navigates directly to the login page."""
        self.navigate_to(login_url)
        return self

    def enter_email(self, email: str) -> "LoginPage":
        """Enters email address into username field."""
        self.send_keys(self._EMAIL_INPUT, email)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """Enters password into password field."""
        self.send_keys(self._PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        """Clicks login submit button."""
        self.click(self._LOGIN_BUTTON)

    def do_login(self, email: str, password: str) -> None:
        """Executes full login submission workflow."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Retrieves text from danger alert banner."""
        return self.get_text(self._ALERT_DANGER)

    def is_error_alert_displayed(self) -> bool:
        """Validates presence of failure warning banner."""
        return self.is_visible(self._ALERT_DANGER, timeout=5)
