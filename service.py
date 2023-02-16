import asyncio
from datetime import timedelta


async def is_valid_time(time: str) -> tuple[int, int] | bool:
    """Валидация времени"""
    try:
        hours, minutes = map(int, time.split(":"))
    except ValueError:
        return False

    if not (6 <= hours <= 11) or not (0 <= minutes <= 59):
        return False

    return hours, minutes


async def add_time(time: str) -> timedelta | bool:
    """Вычисляет время ухода с работы домой"""
    is_valid = await is_valid_time(time)
    if is_valid:
        arrival_time = timedelta(hours=is_valid[0], minutes=is_valid[1])
        working_hours = timedelta(hours=8, minutes=45)
        result = arrival_time + working_hours
        return "{:02d}:{:02d}".format(
            result.seconds // 3600, (result.seconds // 60) % 60
        )
    else:
        return False


if __name__ == "__main__":
    print(asyncio.run(add_time("12:45")))
    print(asyncio.run(add_time("8:46")))
    print(asyncio.run(add_time("hello:46")))
