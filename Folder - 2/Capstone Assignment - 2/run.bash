#!/usr/bin/env bash
# ==============================================================================
# Capstone Assignment 2: Selenium Python Automation Framework Runner
# Candidate: Souvik Nandi (Student ID: 12023002028046)
# Target Application: https://tutorialsninja.com/demo/
# ==============================================================================

set -eo pipefail

# ANSI Color & Formatting Codes
BOLD="\033[1m"
GREEN="\033[0;32m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
CYAN="\033[0;36m"
MAGENTA="\033[0;35m"
NC="\033[0m" # No Color

# Determine project directory (directory of this script)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# Print Header Banner
print_banner() {
    echo -e "${CYAN}==============================================================================${NC}"
    echo -e "${BOLD}${BLUE}   CAPSTONE ASSIGNMENT 2: SELENIUM PYTHON AUTOMATION TEST RUNNER${NC}"
    echo -e "${CYAN}==============================================================================${NC}"
    echo -e " Candidate       : ${BOLD}Souvik Nandi${NC} (Student ID: ${BOLD}12023002028046${NC})"
    echo -e " Email           : ${CYAN}souviknandi19102005@gmail.com${NC}"
    echo -e " Target System   : ${BOLD}https://tutorialsninja.com/demo/${NC}"
    echo -e " Architecture    : ${BOLD}Page Object Model (POM) with Dual Engines (PyTest + Unittest)${NC}"
    echo -e " Project Root    : ${PROJECT_DIR}"
    echo -e "${CYAN}==============================================================================${NC}\n"
}

# Print Usage / Help
show_help() {
    echo -e "${BOLD}Usage:${NC} ./run.bash [OPTION]"
    echo ""
    echo -e "${BOLD}Options:${NC}"
    echo "  --all         (Default) Run both Unittest and PyTest automation suites"
    echo "  --pytest      Run PyTest automation suite only with HTML report"
    echo "  --unittest    Run Unittest automation suite only with HTML report"
    echo "  --install     Setup virtual environment and install all dependencies"
    echo "  --clean       Clean test reports, cache files, and temp artifacts"
    echo "  --open        Open generated HTML test reports in your default browser"
    echo "  --help, -h    Display this help message and exit"
    echo ""
    echo -e "${BOLD}Examples:${NC}"
    echo "  ./run.bash               # Run all tests (Unittest + PyTest)"
    echo "  ./run.bash --pytest      # Run PyTest tests only"
    echo "  ./run.bash --unittest    # Run Unittest tests only"
    echo "  ./run.bash --install     # Install required Python packages"
    echo "  ./run.bash --clean       # Clean old reports and pycache"
    echo "  ./run.bash --open        # Open latest generated reports in browser"
    echo ""
}

# Locate Python 3 Interpreter
detect_python() {
    if command -v python3 &>/dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &>/dev/null; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}[ERROR] Python 3 was not found on your system PATH.${NC}"
        echo -e "${YELLOW}Please install Python 3.8 or higher to run this framework.${NC}"
        exit 1
    fi
}

# Environment & Dependency Setup
setup_environment() {
    detect_python
    echo -e "${BLUE}[INFO] Checking Python environment (${PYTHON_CMD})...${NC}"

    # Check for virtual environment in project root
    if [ -d "$PROJECT_DIR/venv" ]; then
        echo -e "${GREEN}[INFO] Activating existing virtual environment: $PROJECT_DIR/venv${NC}"
        # shellcheck source=/dev/null
        source "$PROJECT_DIR/venv/bin/activate"
        PYTHON_CMD="python"
    elif [ -d "$PROJECT_DIR/.venv" ]; then
        echo -e "${GREEN}[INFO] Activating existing virtual environment: $PROJECT_DIR/.venv${NC}"
        # shellcheck source=/dev/null
        source "$PROJECT_DIR/.venv/bin/activate"
        PYTHON_CMD="python"
    else
        # Check if required libraries are available in active interpreter
        if ! $PYTHON_CMD -c "import selenium, pytest, pytest_html" &>/dev/null; then
            echo -e "${YELLOW}[WARNING] Core dependencies (selenium, pytest, pytest-html) not detected.${NC}"
            echo -e "${BLUE}[INFO] Creating isolated virtual environment at $PROJECT_DIR/venv...${NC}"
            $PYTHON_CMD -m venv "$PROJECT_DIR/venv"
            # shellcheck source=/dev/null
            source "$PROJECT_DIR/venv/bin/activate"
            PYTHON_CMD="python"
            echo -e "${BLUE}[INFO] Upgrading pip and installing dependencies from requirements.txt...${NC}"
            pip install --upgrade pip
            pip install -r "$PROJECT_DIR/requirements.txt"
            echo -e "${GREEN}[INFO] Virtual environment and dependencies successfully configured.${NC}\n"
        else
            echo -e "${GREEN}[INFO] All framework dependencies verified in active Python environment.${NC}"
        fi
    fi
}

# Cleanup Artifacts
clean_artifacts() {
    echo -e "${YELLOW}[INFO] Cleaning temporary files, pycache, and previous reports...${NC}"
    find "$PROJECT_DIR" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find "$PROJECT_DIR" -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    rm -f "$PROJECT_DIR/reports/pytest_report.html" 2>/dev/null || true
    rm -f "$PROJECT_DIR/reports/unittest_report.html" 2>/dev/null || true
    echo -e "${GREEN}[INFO] Cleanup complete.${NC}"
}

# Install Dependencies Explicitly
install_dependencies() {
    detect_python
    echo -e "${BLUE}[INFO] Initializing virtual environment in: $PROJECT_DIR/venv...${NC}"
    $PYTHON_CMD -m venv "$PROJECT_DIR/venv"
    # shellcheck source=/dev/null
    source "$PROJECT_DIR/venv/bin/activate"
    echo -e "${BLUE}[INFO] Upgrading pip...${NC}"
    pip install --upgrade pip
    echo -e "${BLUE}[INFO] Installing packages from requirements.txt...${NC}"
    pip install -r "$PROJECT_DIR/requirements.txt"
    echo -e "${GREEN}${BOLD}[SUCCESS] All dependencies installed successfully into virtual environment!${NC}"
}

# Open Reports in Default System Browser
open_reports() {
    local OPENED=0
    if [ -f "$PROJECT_DIR/reports/pytest_report.html" ]; then
        echo -e "${BLUE}[INFO] Opening PyTest report in browser...${NC}"
        if [[ "$OSTYPE" == "darwin"* ]]; then
            open "$PROJECT_DIR/reports/pytest_report.html"
        elif command -v xdg-open &>/dev/null; then
            xdg-open "$PROJECT_DIR/reports/pytest_report.html"
        fi
        OPENED=1
    fi

    if [ -f "$PROJECT_DIR/reports/unittest_report.html" ]; then
        echo -e "${BLUE}[INFO] Opening Unittest report in browser...${NC}"
        if [[ "$OSTYPE" == "darwin"* ]]; then
            open "$PROJECT_DIR/reports/unittest_report.html"
        elif command -v xdg-open &>/dev/null; then
            xdg-open "$PROJECT_DIR/reports/unittest_report.html"
        fi
        OPENED=1
    fi

    if [ $OPENED -eq 0 ]; then
        echo -e "${YELLOW}[WARNING] No HTML reports found. Please run the tests first: ./run.bash --all${NC}"
    else
        echo -e "${GREEN}[SUCCESS] Reports opened successfully.${NC}"
    fi
}

# Execute Test Suites
execute_tests() {
    local RUNNER_TYPE="$1"
    export PYTHONPATH="$PROJECT_DIR"

    echo -e "${MAGENTA}[RUN] Executing automated test suite: ${BOLD}$RUNNER_TYPE${NC}...\n"
    
    # We do not use set -e here so we can capture exit code and print summary
    set +e
    $PYTHON_CMD "$PROJECT_DIR/run_tests.py" --runner "$RUNNER_TYPE"
    local EXIT_CODE=$?
    set -e

    echo ""
    if [ $EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}${BOLD}==============================================================================${NC}"
        echo -e "${GREEN}${BOLD} ✔ ALL AUTOMATION TESTS PASSED SUCCESSFULLY!${NC}"
        echo -e "${GREEN}${BOLD}==============================================================================${NC}"
    else
        echo -e "${RED}${BOLD}==============================================================================${NC}"
        echo -e "${RED}${BOLD} ✘ TEST RUN COMPLETED WITH FAILURES (Exit code: $EXIT_CODE)${NC}"
        echo -e "${RED}${BOLD}==============================================================================${NC}"
    fi

    echo -e "\n${BOLD}Generated Test Reports & Artifacts:${NC}"
    if [ -f "$PROJECT_DIR/reports/pytest_report.html" ]; then
        echo -e " • PyTest HTML Report   : ${CYAN}file://$PROJECT_DIR/reports/pytest_report.html${NC}"
    fi
    if [ -f "$PROJECT_DIR/reports/unittest_report.html" ]; then
        echo -e " • Unittest HTML Report : ${CYAN}file://$PROJECT_DIR/reports/unittest_report.html${NC}"
    fi
    echo -e " • Screenshots Directory: ${CYAN}file://$PROJECT_DIR/screenshots/${NC}"
    echo -e "\n${YELLOW}Tip: View reports in your browser at any time by running:${NC} ${BOLD}./run.bash --open${NC}\n"

    return $EXIT_CODE
}

# Main Script Dispatcher
main() {
    local ACTION="${1:---all}"

    case "$ACTION" in
        --help|-h)
            print_banner
            show_help
            exit 0
            ;;
        --clean)
            print_banner
            clean_artifacts
            exit 0
            ;;
        --install)
            print_banner
            install_dependencies
            exit 0
            ;;
        --open)
            print_banner
            open_reports
            exit 0
            ;;
        --pytest)
            print_banner
            setup_environment
            execute_tests "pytest"
            exit $?
            ;;
        --unittest)
            print_banner
            setup_environment
            execute_tests "unittest"
            exit $?
            ;;
        --all)
            print_banner
            setup_environment
            execute_tests "all"
            exit $?
            ;;
        *)
            print_banner
            echo -e "${RED}[ERROR] Unrecognized option: $ACTION${NC}\n"
            show_help
            exit 1
            ;;
    esac
}

main "$@"
