import requests
from datetime import datetime, timezone
import smtplib
import time

MY_LAT = 51.507351 # my latitude
MY_LONG = -0.127758 # my longitude

# use your own email and password :p with lowering the security so that smtp may work properly
MY_EMAIL = "********@*****.com"
PASSWORD = "***************"

#Your position is within +5 or -5 degrees of the ISS position.


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LONG-6<=iss_longitude<=MY_LONG+6 and MY_LAT-6<=iss_longitude<=MY_LAT+6:
        return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # {   'results':
    #     {   'sunrise': '2021-02-13T07:16:23+00:00',
    #         'sunset': '2021-02-13T17:12:56+00:00',
    #        'solar_noon': '2021-02-13T12:14:39+00:00',
    #        'day_length': 35793,
    #        'civil_twilight_begin':
    #        '2021-02-13T06:41:50+00:00',
    #        'civil_twilight_end': '2021-02-13T17:47:29+00:00',
    #        'nautical_twilight_begin': '2021-02-13T06:02:41+00:00',
    #        'nautical_twilight_end': '2021-02-13T18:26:38+00:00',
    #        'astronomical_twilight_begin': '2021-02-13T05:24:04+00:00',
    #        'astronomical_twilight_end': '2021-02-13T19:05:15+00:00'         },
    #        'status': 'OK'}

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(timezone.utc)
    if time_now.hour <= sunrise or time_now>=sunset:
        return True

while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look up ☝\n\nLook overhead, ISS is right above in the sky. :)"
                                )

    time.sleep(60)



