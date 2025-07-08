"""test_csv_reader.py"""
from pathlib import Path

from adapters.input.csv_reader import read_csv

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def test_csv_reader_parses_readings():
    """
    Check that CSV reader parses readings correctly.

    :return: List of reading objects.
    """
    file_path = DATA_DIR / "2016-readings.csv"
    readings = read_csv(str(file_path))
    assert len(readings) == 120
    assert readings[0].client_id == "583ef6329d7b9"
    assert readings[0].period_year == "2016"
    assert readings[0].period_month == "01"
    assert readings[0].value == 42451
    assert readings[119].client_id == "583ef6329da0b"
    assert readings[119].period_year == "2016"
    assert readings[119].period_month == "12"
    assert readings[119].value == 29129
