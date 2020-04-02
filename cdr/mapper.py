#!/usr/bin/env python
"""mapper.py"""
import sys
from datetime import datetime


def toMinuts(date1, date2):
    date_time = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    date_time2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    return (date_time2 - date_time).total_seconds() / 60


def map():
    for line in sys.stdin.readlines():
        line = line.strip().split("|")
        callDurationInMinutes = toMinuts(line[2], line[3])
        if line[4] == str(1):
            print(line[0], callDurationInMinutes)


if __name__ == '__main__':
    map()
