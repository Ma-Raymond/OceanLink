from flask import Flask
import requests
from FogDetection import *
from Wind import *
from ObjectDetection import *

app = Flask(__name__)

# Route for the API

@app.route('/items/<lat>/<lon>/<distance>/<radius>/<speed>')
def members(lon, lat,distance,radius,speed):
  BASE_URL = "https://www.worldtides.info/api/v3?heights&plot&date=today"
  API_KEY = "41d5394a-51d1-4e80-b236-e31d9d867b0b"
  longitude = lon
  latitude = lat

  url = BASE_URL + "&lat=" + latitude + "&lon=" + longitude + "&key=" + API_KEY

  response = requests.get(url).json()

  heightsMaps = response['heights']
  heightsTotal = 0
  for i in range(len(heightsMaps)):
    heightsTotal += heightsMaps[i]['height']

  heightsAverage = round(heightsTotal / len(heightsMaps), 4)

  return {
    "height": heightsAverage,
    "Fog": fogMain(lon, lat),
    "WindSpeed": windMain()[1],
    "WindComment": windMain()[0],
    "Objects": objectMain(distance, radius, lat, lon,speed),
  }

if __name__ == "__main__":
    app.run(debug=True)