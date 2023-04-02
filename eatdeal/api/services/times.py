import datetime


def get_start_end_times() -> list[tuple[datetime.time, str]]:
    """Функция создания списка возможного временного интервала"""
    hr_interval: tuple = (0, 24)
    min_interval: tuple = (0, 60, 30)
    times: list = []
    for hour in range(*hr_interval):
        for minute in range(*min_interval):
            time = datetime.time(hour, minute)
            times.append((time, f"{time.strftime('%H:%M')}"))
    return times
