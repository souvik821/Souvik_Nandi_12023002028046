import base64
import os
import re
from datetime import datetime
from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver


class ScreenshotUtil:
    """Utility class to handle automated screenshot captures upon test failure or on-demand."""

    @staticmethod
    def _sanitize_filename(name: str) -> str:
        return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

    @staticmethod
    def capture_screenshot(driver: WebDriver, test_name: str) -> str:
        """Captures a PNG screenshot and stores it in the screenshots directory.
        Returns the absolute file path of the saved screenshot.
        """
        if driver is None:
            return ""

        base_dir = Path(__file__).resolve().parent.parent
        screenshots_dir = base_dir / 'screenshots'
        os.makedirs(screenshots_dir, exist_ok=True)

        clean_name = ScreenshotUtil._sanitize_filename(test_name)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
        filename = f"{clean_name}_{timestamp}.png"
        file_path = screenshots_dir / filename

        try:
            driver.save_screenshot(str(file_path))
            return str(file_path)
        except Exception as e:
            print(f"Warning: Failed to capture screenshot for {test_name}: {e}")
            return ""

    @staticmethod
    def capture_base64(driver: WebDriver) -> str:
        """Returns base64 encoded screenshot string for embedding into HTML reports."""
        if driver is None:
            return ""
        try:
            return driver.get_screenshot_as_base64()
        except Exception:
            return ""
