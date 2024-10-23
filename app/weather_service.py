import aiohttp
import asyncio
import time
from app.s3_helper import upload_to_s3, check_cache
from app.dynamodb_helper import log_to_dynamodb
from app.config import *
async def fetch_weather(city: str):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Error fetching weather data for {city}")
            return await response.json()

async def get_weather_data(city: str):
    #check data from cache 
    cached_data = await check_cache(city)
    if cached_data:
        return cached_data

    data = await fetch_weather(city)
    timestamp = int(time.time())
    
    #create file with timestamp
    filename = f"{city}_{timestamp}.json"
    await upload_to_s3(filename, data)

    await log_to_dynamodb(city, timestamp, filename)

    return data
