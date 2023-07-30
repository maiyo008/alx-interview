#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    """
    num_bytes_to_follow = 0

    for num in data:
        # Check if the number is a valid UTF-8 start byte
        if num_bytes_to_follow == 0:
            if num & 0x80 == 0:  # Single-byte character (0xxxxxxx)
                continue
            elif num & 0xE0 == 0xC0:  # Two-byte character (110xxxxx)
                num_bytes_to_follow = 1
            elif num & 0xF0 == 0xE0:  # Three-byte character (1110xxxx)
                num_bytes_to_follow = 2
            elif num & 0xF8 == 0xF0:  # Four-byte character (11110xxx)
                num_bytes_to_follow = 3
            else:
                return False
        else:
            # Check if the number is a valid UTF-8 follow byte (10xxxxxx)
            if num & 0xC0 != 0x80:
                return False

            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
