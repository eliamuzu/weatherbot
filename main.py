from pyowm.owm import OWM
from datetime import datetime
from dotenv import load_dotenv
import os
import twitter

# loading all environment variables needed
load_dotenv()
OWM_KEY = os.getenv('OWM_API_KEY')
API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET =  os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
LOCATION = os.getenv('WEATHER_LOCATION', 'Accra')


#authentication for twitter api using tweepy
api = twitter.Api(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, TOKEN_SECRET)
today = datetime.now()

try :
    owm =  OWM(OWM_KEY)
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
        
    api.PostUpdate(current_weather)
    print("tweet posted")

except Exception as e:
    print(f"Error: {e}")
