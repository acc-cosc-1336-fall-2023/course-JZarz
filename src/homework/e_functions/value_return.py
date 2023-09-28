from datetime import time

def get_hour(epoch_seconds):
    hour = epoch_seconds // 3600
    return hour

def get_minutes(epoch_seconds):
    remainder = epoch_seconds // 60
    minutes = remainder % 60
    return minutes


def get_seconds(epoch_seconds):
    remainder_of_hour = epoch_seconds % 3600
    remainder_of_seconds = remainder_of_hour % 60
    return remainder_of_seconds

def timestamp(epoch_seconds):
    hr = get_hour(epoch_seconds)
    min = get_minutes(epoch_seconds)
    sec = get_seconds(epoch_seconds)

    timestamp = time(hr, min, sec)
    print(timestamp)
    


    