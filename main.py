"""main.py: Entry point for running anomaly detection."""

import sys

from app.detect_anomalies import detect_from_file


def main():
    """
    Command-line interface for detecting anomalies from a given file.

    Expects a single command-line argument specifying the path to the input file.
    If the argument is missing or incorrect, prints usage instructions and exits.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: python cli.py <file>")
        sys.exit(1)
    detect_from_file(sys.argv[1])

if __name__ == "__main__":
    main()
