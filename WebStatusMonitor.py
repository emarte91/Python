import requests
import time
import datetime

while True:
    r = requests.get("https://thinktreeit.com")
    if r.status_code != 200:
        print(f'Down Status Code:{r.status_code} {datetime.datetime.now()}')
        time.sleep(5)
    else:
        print("Website back up!")
        break
