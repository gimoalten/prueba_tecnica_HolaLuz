"""test_xml_reader.py"""
from pathlib import Path

from adapters.input.xml_reader import read_xml

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def test_xml_reader_parses_readings():
    """
    Check that XML reader parses readings correctly.

    :return: List of reading objects.
    """
    file_path = DATA_DIR / "2016-readings.xml"
    readings = read_xml(str(file_path))
    assert len(readings) == 120
    assert readings[0].client_id == "583ef6329df6b"
    assert readings[0].period_year == "2016"
    assert readings[0].period_month == "01"
    assert readings[0].value == 37232
    assert readings[119].client_id == "583ef6329e41b"
    assert readings[119].period_year == "2016"
    assert readings[119].period_month == "12"
    assert readings[119].value == 31537
