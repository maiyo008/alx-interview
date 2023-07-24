#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    """
    isUTF = []
    for d in data:
        bin_rep = bin(d)[2:]
        if d >= 0 and d < 128:
            if bin_rep[0] == 0 or len(bin_rep) < 8:
                print("UTF-8, 1 byte")
                isUTF.append(True)
            else:
                isUTF.append(False)
        if d >= 128 and d < 2048:
            
        else:
            isUTF.append(False)
    if False not in isUTF:
        return True
    else:
        return False
