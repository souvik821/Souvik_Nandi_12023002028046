import os
import sys
from pathlib import Path
import pytest

# Ensure project root is in sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.driver_factory import DriverFactory
from utils.screenshot_util import ScreenshotUtil
from utils.config_reader import ConfigReader


@pytest.fixture(scope="class")
def driver(request):
    """Initializes a clean WebDriver instance per test class and guarantees teardown."""
    drv = DriverFactory.create_driver()
    if request.cls:
        request.cls.driver = drv

    yield drv

    # Teardown: Safely terminate browser instance
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """PyTest hook wrapper that intercepts test execution to capture failure screenshots
    and embed them directly into the generated HTML report.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        drv = getattr(item, "driver", None)
        if drv is None and getattr(item, "cls", None) is not None:
            drv = getattr(item.cls, "driver", None)
        if drv is not None:
            # 1. Save PNG screenshot on filesystem
            screenshot_path = ScreenshotUtil.capture_screenshot(drv, item.name)

            # 2. Embed into pytest-html report
            try:
                import pytest_html
                base64_img = ScreenshotUtil.capture_base64(drv)
                if base64_img:
                    extra.append(pytest_html.extras.image(base64_img, name="Failure Viewport"))
                if screenshot_path:
                    rel_path = os.path.relpath(screenshot_path, item.config.rootpath)
                    html_snippet = f'<div style="margin: 8px 0;"><strong>Screenshot File:</strong> <a href="{rel_path}" target="_blank">{os.path.basename(screenshot_path)}</a></div>'
                    extra.append(pytest_html.extras.html(html_snippet))
            except Exception as e:
                print(f"Warning attaching screenshot to HTML report: {e}")

    report.extra = extra


def pytest_html_report_title(report):
    report.title = "Capstone Automation Execution Report — E-Commerce (PyTest + POM)"
