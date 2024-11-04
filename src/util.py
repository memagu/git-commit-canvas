from datetime import datetime, timedelta
from typing import Optional

def get_weekday(date: datetime, sunday_is_zero: bool = True) -> int:
    if sunday_is_zero:
        return date.isoweekday() % 7
    else:
        return date.weekday()

def week_and_weekday_to_date(week: int, weekday: int, year: Optional[int] = None, sunday_is_zero: bool = True) -> Optional[datetime]:
    year = year or datetime.now().year

    first_date = datetime(year, 1, 1)
    last_date = datetime(year, 12, 31)

    date = first_date + timedelta(weekday - get_weekday(first_date, sunday_is_zero) + 7 * week)
    if first_date <= date <= last_date:
        return date
    else:
        return None
