#!/usr/bin/env python
"""mapper.py"""
import sys

USER_ID = 0
TRACK_ID = 1
IS_SCROBBLED = 2
RADIO = 3
IS_SKIPPED = 4
for line in sys.stdin.readlines():
    line = line.strip().split("|")
    if len(line) == 5:
        print(line[TRACK_ID], line[USER_ID])
