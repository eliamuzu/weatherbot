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


#authentication for twitter api using tweepy
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)


#Weather condition generaation
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

    
    current_weather = f" \n. Good morning! Welcome to your local weather forecast for {today}.\n We are starting the day off with {weather_status} and a temperature of {weather_temp['temp']} degrees.\n It feels like {weather_temp['feels_like']} outside.\nWe have winds moving at {weather_wind['speed']} mph\n"

except Exception as e:
    print(f"Error: {e}")


try:
    api.update_status(current_weather)
except Exception as e:
    print(f"Error: {e}")