import asyncio
from datetime import timedelta


async def is_valid_time(time: str):
    time_parts = time.split(":")
    if len(time_parts) != 2:
        return False

    hours, minutes = time_parts
    if not hours.isdigit() or not minutes.isdigit():
        return False

    hours = int(hours)
    minutes = int(minutes)
    if hours < 6 or hours > 11:
        return False
    if minutes < 0 or minutes > 59:
        return False

    return hours, minutes


async def add_time(time: str) -> timedelta | bool:
    is_valid = await is_valid_time(time)
    if is_valid:
        tm3 = timedelta(hours=is_valid[0], minutes=is_valid[1])
        tm4 = timedelta(hours=8, minutes=45)
        sum1 = str(tm3 + tm4).split(":")
        return f"{sum1[0]}:{sum1[1]}"
    else:
        return False


if __name__ == "__main__":
    print(asyncio.run(add_time("12:45")))
    print(asyncio.run(add_time("8:46")))
    print(asyncio.run(add_time("hello:46")))
