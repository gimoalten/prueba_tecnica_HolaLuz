"""detect_anomalies.py: Orchestrates the anomaly detection process based on input file format."""

from typing import List

from adapters.input.csv_reader import read_csv
from adapters.input.xml_reader import read_xml
from adapters.output.console_writer import present_readings
from domain.models import SuspiciousReading
from domain.services import detect_anomalies


def detect_from_file(file_path: str) -> List[SuspiciousReading]:
    """
    Detects anomalous readings from a given input file (CSV or XML) and prints them.

    This function reads the input file, determines the format based on its extension,
    parses the data into Reading objects, detects suspicious readings, and prints the
    results in a formatted table.

    Args:
        file_path (str): Path to the input file (.csv or .xml).

    Raises:
        ValueError: If the file extension is not supported.

    Returns:
        None
    """
    if file_path.endswith('.csv'):
        readings = read_csv(file_path)
    elif file_path.endswith('.xml'):
        readings = read_xml(file_path)
    else:
        raise ValueError("Unsupported file format")

    suspicious = detect_anomalies(readings)
    present_readings(suspicious)
    return suspicious
