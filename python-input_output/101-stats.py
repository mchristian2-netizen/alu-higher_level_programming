#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the current statistics.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary of status codes and their counts.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """
    Parses a single line and updates statistics.

    Args:
        line (str): The line to parse.
        total_size (int): The current total file size.
        status_codes (dict): The current status code counts.

    Returns:
        tuple: Updated (total_size, status_codes).
    """
    parts = line.split()
    if len(parts) >= 7:
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
        except (ValueError, IndexError):
            pass
    return total_size, status_codes


def main():
    """Main entry point for the log parsing script."""
    total_size = 0
    line_count = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(line, total_size, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
