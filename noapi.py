import random
import time
import requests
import datetime



def noapi(url,min,max):
    current_date = datetime.datetime.now()

    try:
        # generating random delays to sleep
        random_delay = random.randint(min,max)

        print(f'[{current_date.strftime("%H:%M:%S")}] [INFO] Running without API')
        response = requests.get(url);

        print(f"Sleeping for {random_delay}s")
        time.sleep(random_delay)

        #Sending response back on 200 success
        if response.status_code==200:
            print(f"{current_date.strftime('%H:%M:%S')}] [INFO] No API request Successful.")

            return response.text
        print(f"{current_date.strftime('%H:%M:%S')}] [INFO] Your IP might be block by Google.")

    except Exception as e:
        print(f'[{current_date.strftime("%H:%M:%S")}] [INFO] {e}')
    return None

