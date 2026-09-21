import sys
from pathlib import Path
import pytest

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader


class TestLoginPyTest:
    """PyTest Suite for E-Commerce User Authentication (POM + Data-Driven)."""

    @pytest.mark.parametrize("case", CSVReader.get_login_test_data(), ids=lambda c: c["test_case_id"])
    def test_login_data_driven(self, driver, case):
        """Data-driven login test executing scenarios from login_data.csv."""
        config = ConfigReader()
        login_page = LoginPage(driver)
        my_account_page = MyAccountPage(driver)

        # 1. Navigate to Login Page
        login_page.open(config.login_url)

        # 2. Perform Login with CSV inputs
        login_page.do_login(case["email"], case["password"])

        # 3. Dynamic Assertions based on Expected Status
        if case["expected_status"].upper() == "SUCCESS":
            # Positive validation: User must land on My Account dashboard
            assert my_account_page.is_account_page_displayed(), (
                f"Expected My Account dashboard for {case['test_case_id']}, but not displayed."
            )
            heading = my_account_page.get_header_text()
            assert case["expected_message"] in heading, (
                f"Expected '{case['expected_message']}' in heading, found: '{heading}'"
            )
            # Clean teardown: Log out after positive test
            my_account_page.click_logout()

        else:
            # Negative validation: Error alert banner must be displayed
            assert login_page.is_error_alert_displayed(), (
                f"Expected error alert for invalid login in {case['test_case_id']}, but none appeared."
            )
            error_text = login_page.get_error_message()
            # OpenCart returns either standard credential warning or rate-limiting warning after repeated attempts
            expected_tokens = [
                case["expected_message"],
                "Warning: Your account has exceeded allowed number of login attempts",
                "Warning: No match for E-Mail Address",
                "Warning:"
            ]
            assert any(token in error_text for token in expected_tokens), (
                f"Expected error alert warning for {case['test_case_id']}, but got: '{error_text}'"
            )
