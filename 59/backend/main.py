from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from typing import Optional
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app_geocode = FastAPI(
    title="Geocode API",
    description="This API allows for geocoding and reverse geocoding functionalities.",
    version="1.0.0",
)

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
print(GOOGLE_MAPS_API_KEY)
GOOGLE_MAPS_GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"

@app_geocode.get("/geocode", operation_id="geocodeAddress", summary="Geocode an address to get its latitude and longitude.")
async def geocode(address: str):
    # Prepare the request parameters
    params = {"key": GOOGLE_MAPS_API_KEY, "address": address}

    # Make a request to the Google Maps Geocoding API
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_MAPS_GEOCODING_URL, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error from Google Maps API")

    # Parse the response and extract the relevant data
    data = response.json()
    if data["status"] == "OK":
        result = data["results"][0]
        formatted_address = result["formatted_address"]
        lat = result["geometry"]["location"]["lat"]
        lng = result["geometry"]["location"]["lng"]
        return JSONResponse(content={"address": formatted_address, "lat": lat, "lng": lng})
    else:
        raise HTTPException(status_code=400, detail=data["error_message"])

@app_geocode.get("/reverse", operation_id="reverseGeocode", summary="Reverse geocode coordinates to get the corresponding address.")
async def reverse_geocode(latlng: str):
    # Prepare the request parameters
    params = {"key": GOOGLE_MAPS_API_KEY, "latlng": latlng}

    # Make a request to the Google Maps Geocoding API
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_MAPS_GEOCODING_URL, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error from Google Maps API")

    # Parse the response and extract the relevant data
    data = response.json()
    if data["status"] == "OK":
        result = data["results"][0]
        formatted_address = result["formatted_address"]
        return JSONResponse(content={"address": formatted_address})
    else:
        raise HTTPException(status_code=400, detail=data["error_message"])

if __name__ == "__main__":
    uvicorn.run("main:app_geocode", host="0.0.0.0", port=4319)