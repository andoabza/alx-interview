#!/usr/bin/python3
'''parse log file and print stats'''
import sys
import signal
import re
from collections import defaultdict


total_size = 0
status_counts = defaultdict(int)
lines_processed = 0


def handle_interrupt(signum, frame):
    # Print statistics and exit on interrupt
    print("Total file size: ", total_size)
    for status_code, count in status_counts.items():
        print(f"{status_code}: {count}")
    sys.exit()

signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    lines_processed += 1
    match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
    if match:
        ip_address, status_code, file_size = match.groups()
        total_size += int(file_size)
        status_counts[status_code] += 1
        if lines_processed % 10 == 0:
            print("Total file size: ", total_size)
            for status_code, count in status_counts.items():
                print(f"{status_code}: {count}")