# Souvik Nandi (12023002028046) - Python Automation & Quality Assurance Portfolio

![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.14-blue.svg)
![Selenium WebDriver](https://img.shields.io/badge/Selenium-4.x-brightgreen.svg)
![PyTest](https://img.shields.io/badge/PyTest-9.x-orange.svg)
![Unittest](https://img.shields.io/badge/Unittest-Framework-yellow.svg)
![Architecture](https://img.shields.io/badge/Architecture-Page_Object_Model_(POM)-purple.svg)
![Status](https://img.shields.io/badge/Status-Passing_100%25-brightgreen.svg)

---

## 📌 Student Credentials
- **Name:** Souvik Nandi
- **Enrollment ID:** `12023002028046`
- **Email:** [souviknandi19102005@gmail.com](mailto:souviknandi19102005@gmail.com)
- **Department:** Computer Science & Engineering (Artificial Intelligence & Machine Learning)
- **Academic Session:** 2023–2027
- **GitHub Repository:** [https://github.com/souvik821/Souvik_Nandi_12023002028046](https://github.com/souvik821/Souvik_Nandi_12023002028046)

---

## 📂 Repository Structure

```text
Souvik_Nandi_12023002028046/
├── run.bash                                 # Root All-in-One Bash Test Runner
├── run.sh                                   # Alias for run.bash
├── run_capstone.sh                          # Alias for run.bash
│
├── Folder - 1/                              # Core Lab Assignments
│   ├── Module - 1/                          # Assignments 1 through 6 (Laboratory Records)
│   └── Module - 2/                          # Assignments 7 through 9 (Laboratory Records)
│
├── Folder - 2/                              # Capstone Project
│   ├── README.md                            # Capstone documentation
│   ├── Souvik_Nandi_12023002028046(Capstone_Assignment_2).pdf  # 4-page Academic Lab Report
│   └── Capstone Assignment - 2/             # Selenium Automation Framework Codebase
│       ├── run.bash                         # All-in-one test execution bash script
│       ├── run.sh                           # Symlink to run.bash
│       ├── run_tests.py                     # Python CLI test dispatcher
│       ├── requirements.txt                 # Project dependencies
│       ├── pytest.ini                       # Pytest configuration
│       ├── config/                          # config.ini (Environment, timeouts, URLs)
│       ├── pages/                           # Page Object Model classes
│       ├── test_data/                       # External CSV data files (login, search)
│       ├── tests/                           # Pytest & Unittest test suites
│       ├── utils/                           # WebDriver factory, CSV reader, config reader, screenshots
│       ├── screenshots/                     # Real execution screenshots
│       └── reports/                         # Interactive HTML test execution reports
│
└── Folder - 3/                              # Course Certifications
    ├── Certificate - 1/                     # NPTEL / Industrial Certification PDF & README
    └── Certificate - 2/                     # Certification PDF & README
```

---

## 🚀 One-Command Execution (Bash Runner)

You can run the full test suite directly from the repository root:

```bash
# Make executable (if needed):
chmod +x run.bash

# Run all test suites with visible Chrome UI window (Default):
./run.bash

# Or run specific test runners with visible UI:
./run.bash --pytest       # Run PyTest suite with visible Chrome UI
./run.bash --unittest     # Run Unittest suite with visible Chrome UI
./run.bash --headless     # Run silently in background without browser window
./run.bash --install      # Auto-setup virtual environment & dependencies
./run.bash --clean        # Clean old reports and pycache
./run.bash --open         # Open generated HTML test reports in your default browser
```

*(Supported aliases: `./run.sh`, `bash run.bash`, or `./run_capstone.sh`)*

---

## 📊 Capstone Target Application
- **Platform:** [TutorialsNinja E-Commerce Demo](https://tutorialsninja.com/demo/)
- **Modules Covered:**
  - User Authentication (Login: Valid credentials, Invalid passwords, Unregistered email, Rate-limiting validation)
  - Product Catalog Discovery (Search: Existing items `MacBook`, `iPhone`, `Samsung`, Non-existent items, Special characters)
- **Reporting:** Standalone interactive HTML reports generated at `Folder - 2/Capstone Assignment - 2/reports/` with 100% pass rate.
