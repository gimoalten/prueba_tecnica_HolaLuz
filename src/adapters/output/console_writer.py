"""console_writer.py: Handles formatted console output for suspicious readings."""

from tabulate import tabulate

from domain.models import SuspiciousReading


def present_readings(readings: list[SuspiciousReading]) -> None:
    """
    Displays a table of suspicious readings in the console.

    Each row includes the client ID, the month, the suspicious value, and
    the median used to flag the anomaly.

    Args:
        readings (list[SuspiciousReading]): A list of SuspiciousReading instances to display.

    Returns:
        None
    """
    table = [
        [reading.client_id, reading.month, reading.suspicious_value, round(reading.median, 2)]
        for reading in readings
    ]
    print(tabulate(table, headers=["Client", "Month", "Suspicious", "Median"]))
