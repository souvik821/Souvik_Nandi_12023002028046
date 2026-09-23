import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.screenshot_util import ScreenshotUtil


class TestLoginUnittest(unittest.TestCase):
    """Unittest Framework Test Case for Login Workflows with POM and Failure Screenshot hooks."""

    @classmethod
    def setUpClass(cls):
        cls.config = ConfigReader()
        cls.driver = DriverFactory.create_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.my_account_page = MyAccountPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'driver') and cls.driver:
            cls.driver.quit()

    def setUp(self):
        # Clear cookies between test methods to ensure clean authentication state
        self.driver.delete_all_cookies()

    def tearDown(self):
        try:
            # Automated Screenshot on Unittest Failure
            res = getattr(self._outcome, 'result', None)
            if res:
                has_failed = any(test == self for test, _ in getattr(res, 'failures', []) + getattr(res, 'errors', []))
                if has_failed:
                    ScreenshotUtil.capture_screenshot(self.driver, f"unittest_{self._testMethodName}")
        except Exception as e:
            print(f"Warning in tearDown screenshot hook: {e}")

    def test_valid_login(self):
        """Verify valid user login routes to My Account dashboard."""
        self.login_page.open(self.config.login_url)
        self.login_page.do_login(self.config.valid_email, self.config.valid_password)

        self.assertTrue(
            self.my_account_page.is_account_page_displayed(),
            "My Account dashboard should be displayed after valid authentication."
        )
        self.assertIn("My Account", self.my_account_page.get_header_text())
        self.my_account_page.click_logout()

    def test_invalid_password(self):
        """Verify login with invalid password triggers warning alert banner."""
        self.login_page.open(self.config.login_url)
        self.login_page.do_login(self.config.valid_email, "InvalidPassword999!")

        self.assertTrue(
            self.login_page.is_error_alert_displayed(),
            "Warning alert banner should be rendered for incorrect password."
        )
        err = self.login_page.get_error_message()
        self.assertTrue(
            any(t in err for t in ["Warning: No match for E-Mail Address", "Warning: Your account has exceeded", "Warning:"]),
            f"Unexpected error message received: '{err}'"
        )

    def test_unregistered_email(self):
        """Verify login with non-existent email triggers warning alert banner."""
        self.login_page.open(self.config.login_url)
        self.login_page.do_login("nonexistent_account_test@domain.com", "SomePassword123!")

        self.assertTrue(
            self.login_page.is_error_alert_displayed(),
            "Warning banner should be displayed for non-registered user."
        )
        err = self.login_page.get_error_message()
        self.assertTrue(
            any(t in err for t in ["Warning: No match for E-Mail Address", "Warning: Your account has exceeded", "Warning:"]),
            f"Unexpected error message received: '{err}'"
        )

    def test_data_driven_csv_login(self):
        """Iterate through login_data.csv records in Unittest."""
        test_records = CSVReader.get_login_test_data()
        for record in test_records:
            with self.subTest(case=record["test_case_id"]):
                self.login_page.open(self.config.login_url)
                self.login_page.do_login(record["email"], record["password"])

                if record["expected_status"].upper() == "SUCCESS":
                    self.assertTrue(self.my_account_page.is_account_page_displayed())
                    self.my_account_page.click_logout()
                else:
                    self.assertTrue(self.login_page.is_error_alert_displayed())
                    err = self.login_page.get_error_message()
                    self.assertTrue(
                        any(t in err for t in [record["expected_message"], "Warning: Your account has exceeded", "Warning: No match", "Warning:"]),
                        f"Expected warning in error banner for {record['test_case_id']}, got: '{err}'"
                    )


if __name__ == '__main__':
    unittest.main()
