import time


def raiseError(param):
    if not isinstance(param, int | float):
        raise ValueError(f"arg={param} is not Valid Type for this function")


def sys_time():
    t1 = time.localtime()
    return time.strftime("%a, %d %b %Y, %H:%M:%S", t1)


def mintosec(minutes: int | float) -> int | float:
    raiseError(minutes)
    return minutes * 60


def htosec(hours: int | float) -> int | float:
    raiseError(hours)
    return hours * 60 * 60


def daytosec(days: int | float) -> int | float:
    raiseError(days)
    return days * 24 * 60 * 60


def work_week() -> int | float:
    return 1 * 5 * 24 * 60 * 60


def weektosec(weeks: int | float) -> int | float:
    raiseError(weeks)
    return weeks * 7 * 24 * 60 * 60


def weekend() -> int | float:
    return 2 * 24 * 60 * 60


def monthtosec(months: int | float) -> int | float:
    raiseError(months)
    return months * 30 * 24 * 60 * 60


def yeartosec(years: int | float) -> int | float:
    raiseError(years)
    return years * 365 * 24 * 60 * 60
