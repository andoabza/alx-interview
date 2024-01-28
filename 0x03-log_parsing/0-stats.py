#!/usr/bin/python3
'''parse log in stdin'''
import sys


if __name__ == "__main__":
    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0
    size = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                size += int(data[-1])
            except:
                pass
            try:
                if data[-2] in status:
                    status[data[-2]] += 1
            except:
                pass
            if count % 10 == 0:
                print("File size: {}".format(size))
                for key in sorted(status.keys()):
                    if status[key] != 0:
                        print("{}: {}".format(key, status[key]))
    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key in sorted(status.keys()):
            if status[key] != 0:
                print("{}: {}".format(key, status[key]))
        raise
    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key] != 0:
            print("{}: {}".format(key, status[key]))
