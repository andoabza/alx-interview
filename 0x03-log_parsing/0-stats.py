#!/usr/bin/python3
'''parse log in stdin'''
import sys
import signal


count = 0
size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    '''print stats'''
    print("File size: {}".format(size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    '''handle signal'''
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 9:
            try:
                status_code = int(parts[7])
                file_size = int(parts[8])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                size += file_size
                count += 1
                if count % 10 == 0:
                    print_stats()
            except ValueError:
                continue
except KeyboardInterrupt:
    pass

print_stats()