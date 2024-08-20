#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: A list of integers where each integer represents
    1 byte of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    n_bytes = 0
    for num in data:
        binary_rep = format(num, '#010b')[-8:]
        if n_bytes == 0:
            for bit in binary_rep:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0
