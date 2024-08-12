#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys
import signal


def print_stats(total_size, status_codes):
    """
    Print the computed statistics.

    Args:
    total_size (int): Total file size.
    status_codes (dict): Dictionary containing counts of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    Parse a single line of log input.

    Args:
    line (str): A line from the log input.

    Returns:
    tuple: (file_size, status_code) or (None, None) if the line is invalid.
    """
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return file_size, status_code
    except (ValueError, IndexError):
        return None, None


def main():
    """
    Main function to process log input and compute metrics.
    """
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    def signal_handler(sig, frame):
        """Handle keyboard interruption."""
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
