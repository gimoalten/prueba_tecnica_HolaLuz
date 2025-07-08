"""models.py: Data models for readings and suspicious readings."""

from dataclasses import dataclass


@dataclass
class Reading:
    """
    Represents a monthly reading reported by a client.

    Attributes:
        client_id (str): Unique identifier of the client.
        period_year (str): The year of the reading (e.g., "2025").
        period_month (str): The month of the reading (e.g., "07").
        value (int): The measured reading value for the specified period.
    """
    client_id: str
    period_year: str
    period_month: str
    value: int

@dataclass
class SuspiciousReading:
    """
    Represents a flagged reading that may be anomalous or incorrect.

    Attributes:
        client_id (str): Unique identifier of the client.
        month (str): The month of the suspicious reading.
        suspicious_value (int): The reading value considered suspicious.
        median (float): The calculated median for comparison purposes.
    """
    client_id: str
    month: str
    suspicious_value: int
    median: float
