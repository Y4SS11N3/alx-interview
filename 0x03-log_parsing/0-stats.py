#!/usr/bin/python3
"""
Script for parsing and analyzing HTTP request logs.
"""
import re


def process_log_line(line, total_size, status_code_counts):
    """
    Parses a log line and updates the metrics.
    Args:
        line (str): The input line to process.
        total_size (int): Current total file size.
        status_code_counts (dict): Current status code counts.
    Returns:
        int: The updated total file size.
    """
    pattern = (
        r'\s*\S+\s*'                                # IP address
        r'\s*\[[\d\-\s:\.]+\]\s*'                   # Date
        r'\s*"[^"]*"\s*'                            # Request
        r'\s*(?P<status_code>\S+)\s*'               # Status code
        r'\s*(?P<file_size>\d+)'                    # File size
    )
    match = re.fullmatch(pattern, line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        return total_size + file_size
    return total_size


def display_stats(total_size, status_code_counts):
    """
    Displays the accumulated statistics from the HTTP request log.
    """
    print('File size: {:d}'.format(total_size), flush=True)
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(code, count), flush=True)


def main():
    """
    Main function to start the log parser and analyzer.
    """
    line_count = 0
    total_size = 0
    status_code_counts = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0,
    }
    try:
        while True:
            line = input()
            total_size = process_log_line(line, total_size, status_code_counts)
            line_count += 1
            if line_count % 10 == 0:
                display_stats(total_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        display_stats(total_size, status_code_counts)


if __name__ == '__main__':
    main()
