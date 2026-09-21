import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from pages.search_page import SearchPage
from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.screenshot_util import ScreenshotUtil


class TestSearchUnittest(unittest.TestCase):
    """Unittest Framework Test Case for Product Search Workflows with POM and Failure Screenshot hooks."""

    def setUp(self):
        self.config = ConfigReader()
        self.driver = DriverFactory.create_driver()
        self.search_page = SearchPage(self.driver)

    def tearDown(self):
        try:
            res = getattr(self._outcome, 'result', None)
            if res:
                has_failed = any(test == self for test, _ in getattr(res, 'failures', []) + getattr(res, 'errors', []))
                if has_failed:
                    ScreenshotUtil.capture_screenshot(self.driver, f"unittest_{self._testMethodName}")
        except Exception as e:
            print(f"Warning in tearDown screenshot hook: {e}")
        finally:
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()

    def test_search_existing_product(self):
        """Verify searching for an existing product returns matching catalog items."""
        self.search_page.open(self.config.base_url)
        self.search_page.search_product("MacBook")

        self.assertTrue(self.search_page.has_results(), "Expected product results for MacBook.")
        self.assertTrue(
            self.search_page.is_product_displayed("MacBook"),
            "MacBook must be present in search result titles."
        )

    def test_search_non_existent_product(self):
        """Verify searching for a non-existent product renders empty criteria message."""
        self.search_page.open(self.config.base_url)
        self.search_page.search_product("XYZNonExistentItem999")

        no_result_msg = self.search_page.get_no_product_text()
        self.assertIn(
            "There is no product that matches the search criteria.",
            no_result_msg,
            "Appropriate empty state message should be returned."
        )

    def test_data_driven_csv_search(self):
        """Iterate through search_data.csv records in Unittest."""
        test_records = CSVReader.get_search_test_data()
        for record in test_records:
            with self.subTest(case=record["test_case_id"]):
                self.search_page.open(self.config.base_url)
                self.search_page.search_product(record["search_term"])

                if record["expected_status"].upper() == "FOUND":
                    self.assertTrue(self.search_page.has_results())
                    self.assertTrue(self.search_page.is_product_displayed(record["expected_result"]))
                else:
                    self.assertIn(record["expected_result"], self.search_page.get_no_product_text())


if __name__ == '__main__':
    unittest.main()
