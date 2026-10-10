#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to data.json and return success status."""
    try:
        with open(filename, mode="r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, OSError, csv.Error, UnicodeError, TypeError):
        return False
