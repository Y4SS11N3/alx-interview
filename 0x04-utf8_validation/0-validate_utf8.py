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
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            while byte & mask1:
                n_bytes += 1
                mask1 = mask1 >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
