#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys
import re


def print_stats(total_size, status_codes):
    """Print the computed statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """Main function to process log input and compute metrics."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    pattern = r'^(\S+) - \[(.+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
                
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                line_count += 1
                
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
            
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
