#!/usr/bin/python3

import sys
import signal
import re

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


# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
def check_format(input_string):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET \/projects\/\d+ HTTP\/1\.1" \d+ \d+$'
    match = re.match(pattern, input_string)
    return match is not None


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    for line in sys.stdin:
        try:
            if not check_format(line):
                continue
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
