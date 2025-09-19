from pyowm.owm import OWM
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('OWM_API_KEY')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

location = input("What city are you in? ")
today = datetime.now()

try :
    owm =  OWM(API_KEY)
    weather_manager = owm.weather_manager()
    observation = weather_manager.weather_at_place(location)
    w = observation.weather


    weather_status = w.detailed_status
    weather_wind = w.wind()
    weather_humidity = w.humidity
    weather_temp = w.temperature('celsius')

    print(
        f" \n"
        f"Good morning! Welcome to your local weather forecast for {today}.\n"
        f"We are starting the day off with {weather_status} and a temperature of {weather_temp['temp']} degrees.\n"
        f"It feels like {weather_temp['feels_like']} outside.\n" 
        f"We have winds moving at {weather_wind['speed']} mph\n"
) 
except Exception as e:
    print(f"Error: {e}")
