import sys
from pathlib import Path
import pytest

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from pages.search_page import SearchPage
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader


class TestSearchPyTest:
    """PyTest Suite for Product Catalog Search (POM + Data-Driven)."""

    @pytest.mark.parametrize("case", CSVReader.get_search_test_data(), ids=lambda c: c["test_case_id"])
    def test_search_data_driven(self, driver, case):
        """Data-driven product search testing against search_data.csv."""
        config = ConfigReader()
        search_page = SearchPage(driver)

        # 1. Navigate to Store Front
        search_page.open(config.base_url)

        # 2. Execute Product Search
        search_page.search_product(case["search_term"])

        # 3. Evaluate Assertions
        if case["expected_status"].upper() == "FOUND":
            assert search_page.has_results(), (
                f"Expected products for keyword '{case['search_term']}', but no product layouts found."
            )
            assert search_page.is_product_displayed(case["expected_result"]), (
                f"Expected '{case['expected_result']}' in search results for keyword '{case['search_term']}'"
            )
        else:
            no_prod_text = search_page.get_no_product_text()
            assert case["expected_result"] in no_prod_text, (
                f"Expected empty search message '{case['expected_result']}', got: '{no_prod_text}'"
            )
