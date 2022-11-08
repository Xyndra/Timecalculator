import time


def sys_time():
    t1 = time.localtime()
    return time.strftime("%a, %d %b %Y, %H:%M:%S", t1)


def mintosec(minutes: int | float) -> int | float:
    return minutes * 60


def htosec(hours: int | float) -> int | float:
    return hours * 60 * 60


def daytosec(days: int | float) -> int | float:
    return days * 24 * 60 * 60


def work_week() -> int | float:
    return 1 * 5 * 24 * 60 * 60


def weektosec(weeks: int | float) -> int | float:
    return weeks * 7 * 24 * 60 * 60


def weekend() -> int | float:
    return 2 * 24 * 60 * 60


def monthtosec(months: int | float) -> int | float:
    return months * 30 * 24 * 60 * 60


def yeartosec(years: int | float) -> int | float:
    return years * 365 * 24 * 60 * 60
