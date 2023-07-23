#!/usr/bin/python3
"""
Log parsing
"""
import sys
from collections import defaultdict


def main():
    """
    The main program runs from here
    """
    file_sizes = []
    status_counts = defaultdict(int)
    lines_processed = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_line = parse_line(line)
            if parsed_line:
                status_code, file_size = parsed_line
                file_sizes.append(file_size)
                status_counts[status_code] += 1
                lines_processed += 1
                if lines_processed % 10 == 0:
                    print_statistics(file_sizes, status_counts)
    except KeyboardInterrupt:
        print_statistics(file_sizes, status_counts)


def parse_line(line):
    """
    Parses the input from stdin
    """
    parts = line.split(' ')
    if len(parts) != 9 or parts[7]\
            not in ['200', '301', '400', '401', '403', '404', '405', '500']:
        return None
    try:
        file_size = int(parts[8])
    except ValueError:
        return None
    return parts[7], file_size


def print_statistics(file_sizes, status_counts):
    """
    Prints the statistics after every 10 lines,
    or after a keyboard interrupt
    """
    total_size = sum(file_sizes)
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_counts.keys())
    for status_code in sorted_status_codes:
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))


if __name__ == "__main__":
    main()
