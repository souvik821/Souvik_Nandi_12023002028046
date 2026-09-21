import configparser
import os
from pathlib import Path


class ConfigReader:
    """Utility class to load and parse configuration settings from config.ini."""

    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        self._config = configparser.ConfigParser()
        # Find config.ini relative to this file or current working directory
        current_dir = Path(__file__).resolve().parent.parent
        config_path = current_dir / 'config' / 'config.ini'

        if not config_path.exists():
            # Fallback to current working directory
            config_path = Path.cwd() / 'config' / 'config.ini'

        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found at: {config_path}")

        self._config.read(config_path, encoding='utf-8')

    def get(self, section: str, key: str, fallback: str = None) -> str:
        return self._config.get(section, key, fallback=fallback)

    def getint(self, section: str, key: str, fallback: int = 0) -> int:
        return self._config.getint(section, key, fallback=fallback)

    def getboolean(self, section: str, key: str, fallback: bool = False) -> bool:
        return self._config.getboolean(section, key, fallback=fallback)

    # Helper getters
    @property
    def base_url(self) -> str:
        return self.get('app', 'base_url', 'https://tutorialsninja.com/demo/')

    @property
    def login_url(self) -> str:
        return self.get('app', 'login_url', 'https://tutorialsninja.com/demo/index.php?route=account/login')

    @property
    def browser_name(self) -> str:
        return self.get('browser', 'name', 'chrome').lower()

    @property
    def is_headless(self) -> bool:
        return self.getboolean('browser', 'headless', True)

    @property
    def page_load_strategy(self) -> str:
        return self.get('browser', 'page_load_strategy', 'eager')

    @property
    def explicit_wait(self) -> int:
        return self.getint('timeout', 'explicit_wait', 15)

    @property
    def implicit_wait(self) -> int:
        return self.getint('timeout', 'implicit_wait', 5)

    @property
    def valid_email(self) -> str:
        return self.get('credentials', 'valid_email', 'souvik_capstone_test2026@gmail.com')

    @property
    def valid_password(self) -> str:
        return self.get('credentials', 'valid_password', 'Password123!')

    @property
    def screenshots_dir(self) -> str:
        return self.get('paths', 'screenshots_dir', 'screenshots')

    @property
    def reports_dir(self) -> str:
        return self.get('paths', 'reports_dir', 'reports')
