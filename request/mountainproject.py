from PIL import Image
from decouple import config
import requests
import json

MPKEY = config('MP')

def getRocks():
    baseUrl="https://www.mountainproject.com/data/get-routes-for-lat-lon"
    params={
        "lat": "40.4406",
        "lon": "79.9959°",
        "maxDistance": "100",
        "minDiff": "5.6",
        "maxDiff": "5.14",
        "maxResults": "10",
        "key": MPKEY
    }

    response = requests.request("GET", baseUrl, params=params)
    return response.text
