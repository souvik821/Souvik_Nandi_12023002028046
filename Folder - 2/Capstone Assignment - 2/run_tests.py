#!/usr/bin/env python3
"""Unified Test Execution Runner CLI
Supports executing PyTest, Unittest, or both frameworks with automated HTML report generation.
"""

import argparse
import os
import sys
import time
import unittest
from datetime import datetime
from pathlib import Path


def generate_unittest_html_report(results, report_file, duration, suite_name="Unittest Suite"):
    """Generates a standalone, beautiful HTML report for Unittest execution."""
    passed = results.testsRun - len(results.failures) - len(results.errors)
    failed = len(results.failures)
    errors = len(results.errors)
    total = results.testsRun
    pass_pct = (passed / total * 100) if total > 0 else 0

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Capstone Unittest Execution Report</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 0; padding: 24px; background: #f8fafc; color: #1e293b; }}
        .header {{ background: #0f172a; color: #ffffff; padding: 24px; border-radius: 8px; margin-bottom: 24px; }}
        .header h1 {{ margin: 0 0 8px 0; font-size: 24px; }}
        .header p {{ margin: 4px 0; color: #94a3b8; font-size: 14px; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; margin-bottom: 24px; }}
        .card {{ background: #ffffff; padding: 16px; border-radius: 8px; border: 1px solid #e2e8f0; text-align: center; }}
        .card .num {{ font-size: 28px; font-weight: bold; margin-bottom: 4px; }}
        .card .lbl {{ font-size: 12px; text-transform: uppercase; color: #64748b; font-weight: 600; }}
        .text-pass {{ color: #16a34a; }}
        .text-fail {{ color: #dc2626; }}
        .text-err {{ color: #ea580c; }}
        .text-total {{ color: #2563eb; }}
        table {{ width: 100%; border-collapse: collapse; background: #ffffff; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }}
        th, td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid #e2e8f0; font-size: 14px; }}
        th {{ background: #f1f5f9; font-weight: 600; color: #475569; }}
        .badge {{ display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
        .badge-pass {{ background: #dcfce7; color: #15803d; }}
        .badge-fail {{ background: #fee2e2; color: #b91c1c; }}
        .badge-err {{ background: #ffedd5; color: #c2410c; }}
        pre {{ background: #0f172a; color: #f8fafc; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Capstone Automation: Unittest Execution Report</h1>
        <p>Candidate: <strong>Souvik Nandi</strong> (Student ID: <strong>12023002028046</strong>)</p>
        <p>Target System: <strong>TutorialsNinja E-Commerce Platform</strong></p>
        <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Duration: {duration:.2f}s</p>
    </div>

    <div class="stats">
        <div class="card"><div class="num text-total">{total}</div><div class="lbl">Total Tests</div></div>
        <div class="card"><div class="num text-pass">{passed}</div><div class="lbl">Passed</div></div>
        <div class="card"><div class="num text-fail">{failed}</div><div class="lbl">Failed</div></div>
        <div class="card"><div class="num text-err">{errors}</div><div class="lbl">Errors</div></div>
        <div class="card"><div class="num text-pass">{pass_pct:.1f}%</div><div class="lbl">Pass Rate</div></div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Test Case</th>
                <th>Status</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
"""
    for test, err in results.failures:
        html += f"""
            <tr>
                <td><strong>{test}</strong></td>
                <td><span class="badge badge-fail">FAILED</span></td>
                <td><pre>{err}</pre></td>
            </tr>
        """

    for test, err in results.errors:
        html += f"""
            <tr>
                <td><strong>{test}</strong></td>
                <td><span class="badge badge-err">ERROR</span></td>
                <td><pre>{err}</pre></td>
            </tr>
        """

    if not results.failures and not results.errors:
        html += """
            <tr>
                <td colspan="3" style="text-align: center; color: #16a34a; font-weight: 600; padding: 24px;">
                    All Unittest test cases passed with zero assertions failed.
                </td>
            </tr>
        """

    html += """
        </tbody>
    </table>
</body>
</html>
"""
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Unittest HTML report written to: {report_file}")


def run_unittest_suite():
    print("\n" + "="*60)
    print("EXECUTING UNITTEST AUTOMATION SUITE")
    print("="*60)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    tests_dir = Path(__file__).resolve().parent / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern="test_*_unittest.py"))

    reports_dir = Path(__file__).resolve().parent / 'reports'
    os.makedirs(reports_dir, exist_ok=True)
    report_file = reports_dir / 'unittest_report.html'

    start_time = time.time()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    duration = time.time() - start_time

    generate_unittest_html_report(result, report_file, duration)
    return result.wasSuccessful()


def run_pytest_suite():
    print("\n" + "="*60)
    print("EXECUTING PYTEST AUTOMATION SUITE")
    print("="*60)
    import pytest
    project_root = Path(__file__).resolve().parent
    reports_dir = project_root / 'reports'
    os.makedirs(reports_dir, exist_ok=True)
    report_file = reports_dir / 'pytest_report.html'

    args = [
        str(project_root / 'tests'),
        "-v",
        "-k", "pytest",
        f"--html={report_file}",
        "--self-contained-html"
    ]
    exit_code = pytest.main(args)
    print(f"PyTest HTML report written to: {report_file}")
    return exit_code == 0


def main():
    parser = argparse.ArgumentParser(description="Capstone Automation Framework Test Runner")
    parser.add_argument(
        "--runner",
        choices=["pytest", "unittest", "all"],
        default="all",
        help="Select test runner: 'pytest', 'unittest', or 'all' (default: all)"
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run tests in background (headless) mode without visible browser window"
    )
    parser.add_argument(
        "--headed", "--ui",
        action="store_true",
        default=True,
        help="Run tests with visible browser window UI (default)"
    )
    args = parser.parse_args()

    if args.headless:
        os.environ['HEADLESS'] = 'true'
    else:
        os.environ['HEADLESS'] = 'false'

    project_root = Path(__file__).resolve().parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    success = True
    if args.runner in ["unittest", "all"]:
        u_success = run_unittest_suite()
        success = success and u_success

    if args.runner in ["pytest", "all"]:
        p_success = run_pytest_suite()
        success = success and p_success

    print("\n" + "="*60)
    print(f"FINAL EXECUTION STATUS: {'SUCCESS (ALL PASSED)' if success else 'COMPLETED WITH WARNINGS/FAILURES'}")
    print("="*60)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
