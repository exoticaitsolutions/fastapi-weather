from datetime import datetime, timedelta
import aiofiles

CACHE_DURATION = timedelta(minutes=5)
CACHE_DIR = "/tmp"

async def is_cached(city: str):
    try:
        async with aiofiles.open(f"{CACHE_DIR}/{city}.json", 'r') as f:
            data = await f.read()
            file_time = datetime.fromtimestamp(int(data['timestamp']))
            if datetime.now() - file_time < CACHE_DURATION:
                return data
    except FileNotFoundError:
        return None
    return None
