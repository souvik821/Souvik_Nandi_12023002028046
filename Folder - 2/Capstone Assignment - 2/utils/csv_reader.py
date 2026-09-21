import csv
import os
from pathlib import Path
from typing import List, Dict


class CSVReader:
    """Utility class to read test datasets from CSV files for Data-Driven Testing."""

    @staticmethod
    def read_csv(file_name: str) -> List[Dict[str, str]]:
        """Reads a CSV file from the test_data directory and returns a list of dictionaries."""
        base_dir = Path(__file__).resolve().parent.parent
        file_path = base_dir / 'test_data' / file_name

        if not file_path.exists():
            file_path = Path.cwd() / 'test_data' / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"CSV test data file not found: {file_path}")

        data_rows = []
        with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Strip leading/trailing whitespaces from keys and values
                cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
                data_rows.append(cleaned_row)
        return data_rows

    @staticmethod
    def get_login_test_data() -> List[Dict[str, str]]:
        return CSVReader.read_csv('login_data.csv')

    @staticmethod
    def get_search_test_data() -> List[Dict[str, str]]:
        return CSVReader.read_csv('search_data.csv')
