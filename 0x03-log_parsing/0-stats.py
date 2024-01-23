#!/usr/bin/python3

import sys
import signal

default_handler = None
status_codes = {k: 0 for k in [200, 301, 400, 401, 403, 404, 405, 500]}
total_size = 0
counter = 0


def handler(signum, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    for line in sys.stdin:
        try:
            data = line.split()
            status_code = int(data[-2])
            file_size = int(data[-1])
            status_codes[status_code] += 1
            total_size += file_size
            counter += 1
        except:
            pass
        if counter == 10:
            print_stats(total_size, status_codes)
            counter = 0
