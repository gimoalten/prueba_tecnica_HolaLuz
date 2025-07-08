"""test_services.py"""
from domain.models import Reading
from domain.services import detect_anomalies


def test_detect_anomalies():
    """
    Check detection of an anomalous reading.

    :return: List with one detected anomaly.
    """
    readings = [
        Reading("abc", "2025", f"{i:02d}", val)
        for i, val in enumerate([100, 105, 95, 102, 98, 110, 500, 99, 97, 101, 100, 103], 1)
    ]
    anomalies = detect_anomalies(readings)
    assert len(anomalies) == 1
    assert anomalies[0].client_id == "abc"
    assert anomalies[0].month == "07"
    assert anomalies[0].suspicious_value == 500

def test_detect_suspicious_readings_ignores_normal_values():
    """
    Ensure normal readings are not flagged as anomalies.

    :return: Empty list.
    """
    readings = [
        Reading("client1", "2025", f"{i:02}", 100) for i in range(1, 13)
    ]
    anomalies = detect_anomalies(readings)
    assert not anomalies
