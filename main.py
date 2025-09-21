from pyowm.owm import OWM
from datetime import datetime
from dotenv import load_dotenv
import os
import tweepy

# loading all environment variables needed
load_dotenv()
API_KEY = os.getenv('OWM_API_KEY')
API_SECRET =  os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
LOCATION = os.getenv('WEATHER_LOCATION', 'Accra')


#authentication for twitter api using tweepy
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)


def post_weather():
    today = datetime.now()
    try :
        owm =  OWM(API_KEY)
        weather_manager = owm.weather_manager()
        observation = weather_manager.weather_at_place(LOCATION)
        w = observation.weather


        weather_status = w.detailed_status
        weather_wind = w.wind()
        weather_humidity = w.humidity
        weather_temp = w.temperature('celsius')

        
        current_weather = (
            f"Good morning! Weather forecast for {LOCATION} at {today:%Y-%m-%d %H:%M}.\n"
            f"{weather_status}, {weather_temp['temp']}°C (feels like {weather_temp['feels_like']}°C).\n"
            f"Humidity: {weather_humidity}%. Wind: {weather_wind['speed']} mph."
        )     
           
        api.update_status(current_weather)

    except Exception as e:
        print(f"Error: {e}")

