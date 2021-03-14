import requests
import os
import config

from twilio.rest import Client

api_key = config.api_k
latitude = config.lati
longitude = config.longi

account_sid = config.acc_sid
auth_token = config.auth_t

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
            'lat': latitude,
            'lon': longitude,
            'appid': api_key,
            'exclude': "current,minutely,daily,alerts"
}

response = requests.get(OWM_Endpoint, params=parameters)
data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain= True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="If you are in Passau, Take Umbrella",
        from_='+18587712969',
        to='+4917640564230'
    )
    print(message.status)
