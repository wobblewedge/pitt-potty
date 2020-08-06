from PIL import Image
from datetime import date
from decouple import config
import requests

# Request image from NASA api, process and send to twitter.
today = date.today()

startDate=str(today)
endDate=str(today)
api_key=config('KEY')
url=f'https://api.nasa.gov/DONKI/FLR?startDate={startDate}&endDate={startDate}&api_key={api_key}'


r = requests.get(url)
print(r.status_code)
