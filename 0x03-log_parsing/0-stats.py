#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""
import sys
import re


def extract_info(line):
    """Extracts information from a log line."""
    pattern = (
        r'\s*(\S+)\s*'
        r'\s*\[([^\]]+)\]\s*'
        r'\s*"([^"]*)"\s*'
        r'\s*(\S+)\s*'
        r'\s*(\d+)'
    )
    match = re.fullmatch(pattern, line)
    if match:
        ip, date, request, status_code, file_size = match.groups()
        return {
            'status_code': status_code,
            'file_size': int(file_size)
        }
    return None


def print_stats(total_size, status_codes):
    """Print the computed statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """Main function to process log input and compute metrics."""
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            info = extract_info(line)
            if info:
                total_size += info['file_size']
                if info['status_code'] in status_codes:
                    status_codes[info['status_code']] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
