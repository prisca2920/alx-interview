#!/usr/bin/env python3
"""whether lockboxes can be opened"""


def canUnlockAll(boxes):
    """keys to boxes"""
    if not boxes or type(boxes) is not list:
        return False

    opened = [0]
    for n in opened:
        for key in boxes[n]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(opened) == len(boxes):
        return True
    return False
