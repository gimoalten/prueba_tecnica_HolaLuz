"""csv_reader.py: Parses CSV files to extract client reading data."""

import csv

from domain.models import Reading


def read_csv(file_path: str) -> list[Reading]:
    """
    Reads a CSV file and returns a list of Reading objects.

    The CSV is expected to contain a header with the following columns:
        - 'client': The client ID (str)
        - 'period': A string representing the year and month (e.g., "2025-07")
        - 'reading': The reading value (int)

    Args:
        file_path (str): Path to the CSV file containing the readings.

    Returns:
        list[Reading]: A list of Reading instances parsed from the CSV.
    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [
            Reading(row['client'], row['period'][:4], row['period'][-2:], int(row['reading']))
            for row in reader
        ]
