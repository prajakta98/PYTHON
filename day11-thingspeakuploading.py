import time
import requests
import random
for x in range(0,10):
    sensorVal=random.randint(0,20)
    r=requests.get("https://api.thingspeak.com/update?api_key=7GQI4P2PAPZCL4LG&field1={0}".format(sensorVal))
    print("status code-{0},sr.no-{1},value-{2}".format(r.status_code,x,sensorVal))
    time.sleep(30)