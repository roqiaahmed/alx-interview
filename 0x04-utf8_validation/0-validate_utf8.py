#!/usr/bin/python3

"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    n_bytes = 0
    for num in data:
        bin_num = format(num, "#010b")[-8:]
        if n_bytes == 0:
            for bin in bin_num:
                if bin == "0":
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_num[0] == "1" and bin_num[1] == "0"):
                return False
        n_bytes -= 1
    return n_bytes == 0
