#!/usr/bin/python3
'''parse log file and print stats'''
import sys


def print_stats(file_size, status_codes):
    '''print stats'''
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))