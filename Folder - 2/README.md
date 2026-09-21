# Folder - 2: Capstone Assignment 2

## Selenium Python Automation Framework (Unittest + PyTest + POM)

**Student Name:** Souvik Nandi  
**Enrollment ID:** `12023002028046`  
**Department:** Computer Science & Engineering (AI & ML)  
**Academic Session:** 2023–2027  
**Target Platform:** [TutorialsNinja E-Commerce Demo](https://tutorialsninja.com/demo/)  

---

### 📂 Directory Structure

- **[`Capstone Assignment - 2/`](./Capstone%20Assignment%20-%202/)**: Complete production automation framework codebase.
  - **`pages/`**: Page Object Model (POM) interaction classes (`BasePage`, `LoginPage`, `SearchPage`, `MyAccountPage`, `HeaderPage`).
  - **`tests/`**: Automated test suites for both **PyTest** and **Unittest**.
  - **`utils/`**: Reusable utility components (`DriverFactory`, `ConfigReader`, `CSVReader`, `ScreenshotUtil`).
  - **`config/`**: Central configuration (`config.ini`).
  - **`test_data/`**: External CSV test datasets (`login_data.csv`, `search_data.csv`).
  - **`reports/`**: Self-contained HTML execution dashboards (`pytest_report.html`, `unittest_report.html`).
  - **`screenshots/`**: Automated failure / validation screenshots.
  - **`run_tests.py`**: Unified CLI test runner.
  - **`pytest.ini`**: PyTest configuration file.
  - **`requirements.txt`**: Package dependencies.
- **[`Souvik_Nandi_12023002028046(Capstone_Assignment_2).pdf`](./Souvik_Nandi_12023002028046(Capstone_Assignment_2).pdf)**: Formal Academic Laboratory Record document.

---

### 🚀 Quick Run Instructions

```bash
cd "Folder - 2/Capstone Assignment - 2"
pip install -r requirements.txt

# Run all test suites (PyTest + Unittest) with HTML reports
python run_tests.py --runner all
```
