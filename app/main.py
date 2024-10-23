from fastapi import FastAPI, HTTPException
from app.weather_service import get_weather_data

app = FastAPI()

@app.get("/weather")
async def weather(city: str):
    try:
        weather_info = await get_weather_data(city)
        return weather_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
