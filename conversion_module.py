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

    return time_diff_hours # possible returns  days_diff, time_diff_hours, time_diff_minutes, time_diff_seconds


def get_date(date_time):
    date = date_time.split(' ')
    date = datetime.datetime.strptime(date[0], '%Y-%m-%d')
    year = date.year
    month = date.month
    day = date.day + month * 30
    # on this stage no point to extract time since it iss always 12:00:00 + 00:00
    # possible returns year, month, day
    return  day
