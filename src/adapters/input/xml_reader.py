"""xml_reader.py: Parses XML files to extract client reading data."""

import xml.etree.ElementTree as ET

from domain.models import Reading


def read_xml(file_path: str) -> list[Reading]:
    """
    Parses an XML file and converts its contents into a list of Reading objects.

    The XML is expected to contain multiple <reading> elements, each with:
        - 'clientID' attribute (str)
        - 'period' attribute in the format 'YYY-MM' or similar
        - Inner text containing the integer value of the reading

    Args:
        file_path (str): Path to the XML file containing reading data.

    Returns:
        list[Reading]: A list of Reading instances parsed from the XML.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()
    return [
        Reading(
            reading.attrib['clientID'],
            reading.attrib['period'][:4],  # Fixed to get full year (not just 3 chars)
            reading.attrib['period'][-2:],
            int(reading.text)
        )
        for reading in root.findall('reading')
    ]
