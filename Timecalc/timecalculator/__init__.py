import time
from dataclasses import dataclass
import time


@dataclass
class TimeCaluclator:
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    weekend = 2 * day
    work_week = 5 * day
    week = 7 * day
    month = 30 * day
    year = 365 * day

    def sys_time(self) -> str:
        return time.strftime("%a, %d %b %Y, %H:%M:%S", time.localtime())

    def mintosec(self, minutes: float | int) -> float | int:
        self.raiseError(minutes)
        return minutes * self.minute

    def htosec(self, hours: float | int) -> float | int:
        self.raiseError(hours)
        return hours * self.hour

    def daytosec(self, days: float | int) -> float | int:
        self.raiseError(days)
        return days * self.day

    def weektosec(self, weeks: float | int) -> float | int:
        self.raiseError(weeks)
        return weeks * self.week

    def monthtosec(self, months: float | int) -> float | int:
        self.raiseError(months)
        return months * self.month

    def yeartosec(self, years: float | int) -> float | int:
        self.raiseError(years)
        return years * self.year

    def raiseError(self, param) -> None:
        if not isinstance(param, int | float):
            raise ValueError(f"arg={param} is not Valid Type for this function(should be int or float)")
