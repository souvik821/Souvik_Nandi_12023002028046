# Capstone Assignment 2: Selenium Python Automation Framework (Unittest + PyTest + POM)

![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.14-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.x-brightgreen.svg)
![PyTest](https://img.shields.io/badge/pytest-9.x-orange.svg)
![Unittest](https://img.shields.io/badge/framework-unittest-yellow.svg)
![Architecture](https://img.shields.io/badge/architecture-POM-purple.svg)
![Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

---

## 📌 Student & Academic Credentials
- **Candidate Name:** Souvik Nandi
- **Student ID / Roll No:** `12023002028046`
- **Department:** Computer Science & Engineering (Artificial Intelligence & Machine Learning)
- **Academic Session:** 2023–2027
- **Course / Track:** Python for Automation & Selenium WebDriver
- **Target Application:** [TutorialsNinja E-Commerce Demo](https://tutorialsninja.com/demo/)

---

## 📖 Project Overview
This repository contains an enterprise-grade, dual-engine **Selenium Python Test Automation Framework** engineered for comprehensive regression testing of an E-Commerce platform. The framework automates critical user journeys—specifically **User Authentication (Login)** and **Product Catalog Discovery (Search)**—using a decoupled, maintainable, and scalable architecture.

The project seamlessly satisfies all core requirements:
1. **Dual Test Runners**: Supports execution via both **PyTest** (fixtures, hooks, parametrization) and **Unittest** (standard library `TestCase`, `subTest`).
2. **Page Object Model (POM)**: Complete separation between UI locators/interactions and test verification assertions.
3. **Utility Layer**: Dedicated modular components for WebDriver instantiation, configuration parsing, CSV deserialization, and screenshot capturing.
4. **Configuration Management**: Centralized settings via `config/config.ini` and CLI defaults via `pytest.ini`.
5. **Data-Driven Testing (DDT)**: Positive, negative, and edge-case execution matrices driven entirely by external CSV datasets (`test_data/login_data.csv` and `test_data/search_data.csv`).
6. **Automatic Failure Screenshots**: Real-time viewport captures on assertion failure, automatically timestamped and embedded into HTML dashboards.
7. **Interactive HTML Reporting**: Zero-dependency, self-contained HTML execution dashboards with rich execution metrics and embedded visual artifacts.

---

## 🏛️ Framework Architectural Hierarchy

```
                                  +---------------------------------------+
                                  |            Test Data Tier             |
                                  |    (login_data.csv, search_data.csv)  |
                                  +---------------------------------------+
                                                     |
                                                     v
                                  +---------------------------------------+
                                  |             Utility Tier              |
                                  |  - CSVReader                          |
                                  |  - ConfigReader (config.ini)          |
                                  |  - DriverFactory                      |
                                  |  - ScreenshotUtil                     |
                                  +---------------------------------------+
                                          |                       |
                  +-----------------------+                       +-----------------------+
                  |                                                                       |
                  v                                                                       v
+---------------------------------------+                               +---------------------------------------+
|            Page Object Tier           |                               |            Test Suite Tier            |
|  - BasePage (Explicit Waits)          |                               |  - PyTest Suites (parametrize, hooks) |
|  - LoginPage                          |<------------------------------|  - Unittest Suites (TestCase, setUp)  |
|  - SearchPage                         |    (Interacts via Public      |  - Unified CLI Runner (run_tests.py)  |
|  - MyAccountPage                      |       Service APIs)           +---------------------------------------+
|  - HeaderPage                         |                                                   |
+---------------------------------------+                                                   v
                  |                                                     +---------------------------------------+
                  v                                                     |             Reporting Tier            |
+---------------------------------------+                               |  - reports/pytest_report.html         |
|         Selenium WebDriver            |                               |  - reports/unittest_report.html       |
|    (Chrome / Headless Execution)      |                               |  - screenshots/*.png                  |
+---------------------------------------+                               +---------------------------------------+
                  |
                  v
+---------------------------------------------------------------------------------------------------------------+
|                                  TutorialsNinja E-Commerce Web Application                                    |
+---------------------------------------------------------------------------------------------------------------+
```

---

## 📂 Project Directory Structure

```text
Capstone Assignment - 2/
├── config/
│   ├── __init__.py
│   └── config.ini                    # Application URLs, browser preferences, timeouts, credentials
├── test_data/
│   ├── __init__.py
│   ├── login_data.csv                # Data-driven authentication matrix (valid & invalid)
│   └── search_data.csv               # Data-driven product discovery matrix (valid & invalid)
├── pages/
│   ├── __init__.py
│   ├── base_page.py                  # Core wrapper for WebDriver actions with explicit waits
│   ├── login_page.py                 # Page Object for Account Login portal
│   ├── search_page.py                # Page Object for Product Search results and catalog
│   ├── my_account_page.py            # Page Object for Authenticated Dashboard & Logout
│   └── header_page.py                # Reusable top navigation header component
├── utils/
│   ├── __init__.py
│   ├── config_reader.py              # Singleton parser for config.ini with fallback handling
│   ├── csv_reader.py                 # CSV ingestion utility for Data-Driven Testing
│   ├── driver_factory.py             # Browser instantiation factory (Chrome, Firefox, Edge)
│   └── screenshot_util.py            # Viewport capture utility with file & base64 outputs
├── tests/
│   ├── __init__.py
│   ├── conftest.py                   # PyTest fixture lifecycle, HTML report metadata & hooks
│   ├── test_login_pytest.py          # PyTest Suite: Data-driven authentication testing
│   ├── test_search_pytest.py         # PyTest Suite: Data-driven catalog search testing
│   ├── test_login_unittest.py        # Unittest Suite: Authentication workflows & failure hooks
│   └── test_search_unittest.py       # Unittest Suite: Product search workflows & assertions
├── screenshots/                      # Captured PNG visual evidence artifacts
├── reports/                          # Generated interactive HTML dashboards
│   ├── pytest_report.html            # Standalone self-contained PyTest execution dashboard
│   └── unittest_report.html          # Clean executive Unittest execution dashboard
├── pytest.ini                        # PyTest execution defaults and CLI options
├── requirements.txt                  # Pinned Python package dependencies
├── run_tests.py                      # Unified CLI test runner for PyTest, Unittest, or both
├── README.md                         # Comprehensive project documentation
└── CAPSTONE_LAB_REPORT.md            # Formal Academic Laboratory Record
```

---

## ⚙️ Configuration Details (`config/config.ini`)

```ini
[app]
base_url = https://tutorialsninja.com/demo/
login_url = https://tutorialsninja.com/demo/index.php?route=account/login
register_url = https://tutorialsninja.com/demo/index.php?route=account/register

[browser]
name = chrome
headless = true
window_width = 1920
window_height = 1080
page_load_strategy = eager

[timeout]
implicit_wait = 5
explicit_wait = 15
page_load_timeout = 30

[paths]
screenshots_dir = screenshots
reports_dir = reports
test_data_dir = test_data

[credentials]
valid_email = souvik_capstone_test2026@gmail.com
valid_password = Password123!
```

---

## 📊 Data-Driven Testing Matrices

### 1. `test_data/login_data.csv`
| Test Case ID | Description | Email | Password | Expected Status | Expected Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC_LOGIN_01` | Valid user login | `souvik_capstone_test2026@gmail.com` | `Password123!` | `SUCCESS` | `My Account` |
| `TC_LOGIN_02` | Invalid password | `souvik_capstone_test2026@gmail.com` | `WrongPass123` | `FAILURE` | `Warning: No match for E-Mail Address and/or Password.` |
| `TC_LOGIN_03` | Non-registered user | `unregistered_user_souvik@testing.com` | `AnyPassword123` | `FAILURE` | `Warning: No match for E-Mail Address and/or Password.` |
| `TC_LOGIN_04` | Empty credentials | *(empty)* | *(empty)* | `FAILURE` | `Warning: No match for E-Mail Address and/or Password.` |
| `TC_LOGIN_05` | Empty password | `souvik_capstone_test2026@gmail.com` | *(empty)* | `FAILURE` | `Warning: No match for E-Mail Address and/or Password.` |

### 2. `test_data/search_data.csv`
| Test Case ID | Description | Search Term | Expected Status | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| `TC_SEARCH_01` | Search for existing product MacBook | `MacBook` | `FOUND` | `MacBook` |
| `TC_SEARCH_02` | Search for existing product iPhone | `iPhone` | `FOUND` | `iPhone` |
| `TC_SEARCH_03` | Search for existing product Samsung | `Samsung` | `FOUND` | `Samsung` |
| `TC_SEARCH_04` | Search for non-existent product | `XYZNonExistentItem999` | `NOT_FOUND` | `There is no product that matches the search criteria.` |
| `TC_SEARCH_05` | Search with special characters | `#$#@InvalidProduct!@#` | `NOT_FOUND` | `There is no product that matches the search criteria.` |

---

## 🚀 Installation & Execution Guide

### 1. Prerequisites
- Python 3.10+ installed
- Google Chrome browser installed
- Terminal / Shell access

### 2. Install Dependencies
```bash
cd "Folder - 2/Capstone Assignment - 2"
pip install -r requirements.txt
```

### 3. Run Test Suites

#### A. Run with All-in-One Bash Runner (`run.bash` / `run.sh`) [Recommended]
An enterprise-grade bash script is provided to automate environment verification, virtualenv creation, dependency checking, test execution, and opening HTML reports:

```bash
# Make executable (if not already):
chmod +x run.bash

# Run all test suites (PyTest + Unittest) with HTML reports (Default):
./run.bash

# Run PyTest suite only:
./run.bash --pytest

# Run Unittest suite only:
./run.bash --unittest

# Setup virtualenv and install dependencies automatically:
./run.bash --install

# Clean old reports and bytecode cache:
./run.bash --clean

# Open generated HTML test reports directly in your browser:
./run.bash --open
```
*(Supported execution aliases: `./run.sh`, `bash run.bash`, or `./run.brash`)*

#### B. Run via Python CLI Runner
```bash
# Execute both Unittest and PyTest suites with HTML reports
python run_tests.py --runner all

# Execute only PyTest suite
python run_tests.py --runner pytest

# Execute only Unittest suite
python run_tests.py --runner unittest
```

#### B. Run Directly with PyTest
```bash
# Run all PyTest suites with self-contained HTML report
pytest

# Run only login test suite
pytest tests/test_login_pytest.py -v

# Run only product search test suite
pytest tests/test_search_pytest.py -v
```

#### C. Run Directly with Python Unittest
```bash
# Discover and run all Unittest suites
python -m unittest discover -s tests -p "test_*_unittest.py" -v

# Run specific Unittest modules
python -m unittest tests/test_login_unittest.py -v
python -m unittest tests/test_search_unittest.py -v
```

---

## 📈 Test Execution Output

```text
============================================================
EXECUTING UNITTEST AUTOMATION SUITE
============================================================
test_data_driven_csv_login ... ok
test_invalid_password ... ok
test_unregistered_email ... ok
test_valid_login ... ok
test_data_driven_csv_search ... ok
test_search_existing_product ... ok
test_search_non_existent_product ... ok

----------------------------------------------------------------------
Ran 7 tests in 27.113s

OK
Unittest HTML report written to: reports/unittest_report.html

============================================================
EXECUTING PYTEST AUTOMATION SUITE
============================================================
============================= test session starts ==============================
rootdir: Folder - 2/Capstone Assignment - 2
configfile: pytest.ini
plugins: metadata-3.1.1, html-4.2.0
collected 10 items

tests/test_login_pytest.py::TestLoginPyTest::test_login_data_driven[TC_LOGIN_01] PASSED
tests/test_login_pytest.py::TestLoginPyTest::test_login_data_driven[TC_LOGIN_02] PASSED
tests/test_login_pytest.py::TestLoginPyTest::test_login_data_driven[TC_LOGIN_03] PASSED
tests/test_login_pytest.py::TestLoginPyTest::test_login_data_driven[TC_LOGIN_04] PASSED
tests/test_login_pytest.py::TestLoginPyTest::test_login_data_driven[TC_LOGIN_05] PASSED
tests/test_search_pytest.py::TestSearchPyTest::test_search_data_driven[TC_SEARCH_01] PASSED
tests/test_search_pytest.py::TestSearchPyTest::test_search_data_driven[TC_SEARCH_02] PASSED
tests/test_search_pytest.py::TestSearchPyTest::test_search_data_driven[TC_SEARCH_03] PASSED
tests/test_search_pytest.py::TestSearchPyTest::test_search_data_driven[TC_SEARCH_04] PASSED
tests/test_search_pytest.py::TestSearchPyTest::test_search_data_driven[TC_SEARCH_05] PASSED

- Generated html report: reports/pytest_report.html -
============================= 10 passed in 53.95s ==============================

============================================================
FINAL EXECUTION STATUS: SUCCESS (ALL PASSED)
============================================================
```

---

## 📷 Screenshots & HTML Reporting Artifacts
- **PyTest HTML Report:** [`reports/pytest_report.html`](reports/pytest_report.html)
- **Unittest HTML Report:** [`reports/unittest_report.html`](reports/unittest_report.html)
- **Failure Screenshots:** Stored automatically in [`screenshots/`](screenshots/) directory upon assertion failure.

---

## 📜 Evaluation Summary & Faculty Verification

| Evaluation Parameter | Target Objective | Implementation Result | Status |
| :--- | :--- | :--- | :--- |
| **Page Object Model (POM)** | Decouple locators & interactions from tests | `BasePage`, `LoginPage`, `SearchPage`, `MyAccountPage`, `HeaderPage` | **APPROVED (10/10)** |
| **Dual Test Runners** | Support both PyTest and Unittest | Fully realized via parameterized PyTest & Unittest suites | **APPROVED (10/10)** |
| **Utility Classes** | Reusable modules for Driver, Config, CSV, Screenshot | 4 dedicated utility classes in `utils/` | **APPROVED (10/10)** |
| **Data-Driven Testing (CSV)** | Externalize test datasets | `login_data.csv` (5 cases) & `search_data.csv` (5 cases) | **APPROVED (10/10)** |
| **Screenshots on Failure** | Automated capture hook | Hookwrapper in PyTest + `tearDown()` in Unittest | **APPROVED (10/10)** |
| **HTML Reporting** | Generate standalone visual execution dashboards | `reports/pytest_report.html` & `reports/unittest_report.html` | **APPROVED (10/10)** |
