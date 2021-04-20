# this file contains function performing different conversions

import pandas as pd
import time
import datetime


def format_time_diff(time_diff):
    time_diff = time_diff.split(' ')
    days_diff = int(time_diff[0])
    time_diff = time_diff[2].split('.')
    time_diff = datetime.datetime.strptime(time_diff[0], '%H:%M:%S')
    time_diff_seconds = time_diff.second
    time_diff_minutes = time_diff.minute + time_diff_seconds / 60
    time_diff_hours = time_diff.hour + time_diff_minutes / 60
    days_diff = days_diff + time_diff_hours / 24

    return time_diff_minutes # possible returns  days_diff, time_diff_hours, time_diff_minutes, time_diff_seconds
