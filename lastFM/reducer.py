#!/usr/bin/env python
"""mapper.py"""
import sys

h = {}
keys = []
for line in sys.stdin.readlines():
    TRACK_ID = line.split(" ")[0]
    USER_ID = line.split(" ")[1]
    if h.get(TRACK_ID) is None:
        h[TRACK_ID] = set()
    h.get(TRACK_ID, set()).add(USER_ID)
    if TRACK_ID not in keys:
        keys.append(TRACK_ID)
for key in keys:
    print(key + " " + str(len(h.get(key))))
