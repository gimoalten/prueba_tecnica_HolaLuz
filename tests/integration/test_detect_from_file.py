"""test_detect_from_file.py"""
from pathlib import Path

import pytest

from app.detect_anomalies import detect_from_file

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def test_detect_from_csv_file():
    """
    Check anomaly detection from a CSV file.

    :return: List of detected anomalies.
    """
    file_path = DATA_DIR / "2016-readings.csv"
    anomalies = detect_from_file(str(file_path))
    assert anomalies[0].client_id == "583ef6329d7b9"
    assert anomalies[0].month == "09"
    assert anomalies[0].suspicious_value == 3564
    assert anomalies[1].client_id == "583ef6329d89b"
    assert anomalies[1].month == "09"
    assert anomalies[1].suspicious_value == 162078
    assert anomalies[1].median == 59606.5
    assert anomalies[2].client_id == "583ef6329d89b"
    assert anomalies[2].month == "10"
    assert anomalies[2].suspicious_value == 7759
    assert anomalies[2].median == 59606.5

def test_detect_from_xml_file():
    """
    Check anomaly detection from an XML file.

    :return: List of detected anomalies.
    """
    file_path = DATA_DIR / "2016-readings.xml"
    anomalies = detect_from_file(str(file_path))
    assert anomalies[0].client_id == "583ef6329e237"
    assert anomalies[0].month == "11"
    assert anomalies[0].suspicious_value == 1379
    assert anomalies[0].median == 30132.5
    assert anomalies[1].client_id == "583ef6329e271"
    assert anomalies[1].month == "10"
    assert anomalies[1].suspicious_value == 121208
    assert anomalies[1].median == 21661
    assert anomalies[2].client_id == "583ef6329e3ab"
    assert anomalies[2].month == "11"
    assert anomalies[2].suspicious_value == 6440
    assert anomalies[2].median == 27867.5

def test_detect_from_csv_with_no_anomalies():
    """
    Ensure no anomalies are returned from a clean CSV file.

    :return: Empty list.
    """
    file_path = DATA_DIR / "no_anomalies.csv"
    anomalies = detect_from_file(str(file_path))
    assert not anomalies


def test_unsupported_file_format():
    """
    Ensure error is raised for unsupported file format.

    :return: Raises ValueError.
    """
    file_path = DATA_DIR / "unsupported.txt"
    with pytest.raises(ValueError, match="Unsupported file format"):
        detect_from_file(str(file_path))
