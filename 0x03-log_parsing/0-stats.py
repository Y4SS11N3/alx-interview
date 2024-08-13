#!/usr/bin/python3
"""
Script for parsing and analyzing HTTP request logs.
"""

import re


def parse_log_line(log_line):
    """
    Parses a single line of the HTTP request log.
    """
    pattern_parts = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_data = {
        'status_code': 0,
        'file_size': 0,
    }
    log_pattern = '{}\\-{}{}{}{}\\s*'.format(*pattern_parts)
    match = re.fullmatch(log_pattern, log_line)
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        log_data['status_code'] = status_code
        log_data['file_size'] = file_size
    return log_data


def display_stats(total_size, status_code_counts):
    """
    Displays the accumulated statistics from the HTTP request log.
    """
    print('File size: {:d}'.format(total_size), flush=True)
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(code, count), flush=True)


def process_log_line(line, total_size, status_code_counts):
    """
    Processes a log line and updates the metrics.
    Args:
        line (str): The input line to process.
    Returns:
        int: The updated total file size.
    """
    line_data = parse_log_line(line)
    status_code = line_data.get('status_code', '0')
    if status_code in status_code_counts.keys():
        status_code_counts[status_code] += 1
    return total_size + line_data['file_size']


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
            total_size = process_log_line(
                line,
                total_size,
                status_code_counts,
            )
            line_count += 1
            if line_count % 10 == 0:
                display_stats(total_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        display_stats(total_size, status_code_counts)


if __name__ == '__main__':
    main()
