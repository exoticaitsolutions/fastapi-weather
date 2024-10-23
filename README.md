# FastAPI Weather App

## Description
A FastAPI application that fetches weather data from OpenWeather API, stores responses in S3, logs data to DynamoDB, and caches requests for 5 minutes.

## Features:
- Asynchronous data fetching using `aiohttp`
- AWS S3 integration for storing weather data
- DynamoDB integration for logging requests
- Caching mechanism for recently fetched weather data
- Dockerized setup for easy deployment

## Setup Instructions:

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Use Docker Compose:
   ```bash
   docker-compose up --build
   ```
5. Access the API at `http://localhost:8000/weather?city=London`
