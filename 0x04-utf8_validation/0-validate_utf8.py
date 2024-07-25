#!/usr/bin/env python3
"""checking a valid utf8 code"""


def validUTF8(data) -> bool:
    """checking a valid utf8 code"""
    byt = 0
    for i in data:
        j = 1 << 7
        if not byt:
            while i & j:
                byt += 1
                j >>= 1
            if not byt:
                continue
            if byt == 1 or byt > 4:
                return False
        else:
            if i >> 6 != 0b10:
                return False
        byt -= 1
    return byt == 0
