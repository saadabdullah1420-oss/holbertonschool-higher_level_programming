#!/usr/bin/env python3
"""Generate personalized invitation files from a text template."""

import logging


def generate_invitations(template, attendees):
    """Validate inputs and write one invitation file per attendee."""
    if not isinstance(template, str):
        logging.error(
            "Invalid template type: expected str, got %s.",
            type(template).__name__
        )
        return

    if not isinstance(attendees, list):
        logging.error(
            "Invalid attendees type: expected list, got %s.",
            type(attendees).__name__
        )
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            logging.error(
                "Invalid attendee type: expected dict, got %s.",
                type(attendee).__name__
            )
            return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ("name", "event_title", "event_date", "event_location")

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as error:
            logging.error("Could not write %s: %s", filename, error)
