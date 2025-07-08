"""services.py: Contains business logic for detecting anomalies in client readings."""

from statistics import median
from typing import List

from domain.models import Reading, SuspiciousReading


def detect_anomalies(readings: List[Reading]) -> List[SuspiciousReading]:
    """
    Identifies anomalous readings based on a median-based threshold.

    For each client with at least 12 readings, calculates the median value.
    Any reading outside the range [0.5 * median, 1.5 * median] is considered suspicious.

    Args:
        readings (List[Reading]): A list of Reading instances from one or more clients.

    Returns:
        List[SuspiciousReading]: A list of readings flagged as suspicious, including
        the original value and the calculated median for comparison.
    """
    result = []
    client_map = {}
    for reading in readings:
        client_map.setdefault(reading.client_id, []).append(reading)

    for _, client_readings in client_map.items():
        values = [reading.value for reading in client_readings]
        med = median(values)
        lower = med * 0.5
        upper = med * 1.5
        for reading in client_readings:
            if reading.value < lower or reading.value > upper:
                result.append(SuspiciousReading(reading.client_id,
                                                reading.period_month,
                                                reading.value,
                                                med))
    return result
