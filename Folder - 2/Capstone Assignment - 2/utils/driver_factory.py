from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver

from .config_reader import ConfigReader


class DriverFactory:
    """Factory design pattern implementation for initializing Selenium WebDrivers."""

    @staticmethod
    def create_driver(browser_name: str = None, headless: bool = None) -> WebDriver:
        config = ConfigReader()
        browser = (browser_name or config.browser_name).lower()
        is_headless = config.is_headless if headless is None else headless

        if browser == 'chrome':
            options = ChromeOptions()
            if is_headless:
                options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--ignore-certificate-errors')
            options.page_load_strategy = config.page_load_strategy
            driver = webdriver.Chrome(options=options)

        elif browser == 'firefox':
            options = FirefoxOptions()
            if is_headless:
                options.add_argument('-headless')
            options.page_load_strategy = config.page_load_strategy
            driver = webdriver.Firefox(options=options)

        elif browser == 'edge':
            options = EdgeOptions()
            if is_headless:
                options.add_argument('--headless=new')
            options.page_load_strategy = config.page_load_strategy
            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser requested: {browser}")

        driver.implicitly_wait(config.implicit_wait)
        driver.maximize_window()
        return driver
