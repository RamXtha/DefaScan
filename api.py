import json
import re
import requests
from key import get_key
from screenshot import take_screenshot
import datetime



#Using xenscrape API
def zenscrape(url):
    current_date = datetime.datetime.now()


    #getting api key from key.json file
    api_key = get_key('zenscrape')

    if not api_key:
        return None


    #headers and parameters for zenscrape api request
    headers = { 
        "apikey": api_key
    }

    params = (
    ("url",url),
    );
    try:
        #preareing three requests at max if the request fails
        for tries in range (1,4):
            response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params);
            if response.status_code==200:
                print(f'[{current_date.strftime("%H:%M:%S")}] [info] ScrapperAPI request call successful.')

                #returning the result if status code is 200 ok
                return response.text
            print(f'[{current_date.strftime("%H:%M:%S")}] [info] Retrying API calls...')


        # printing error when response is not 200
        if response.status_code==403:

            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Zenscrape Error! Forbidden -- API key is wrong, you don\'t have enough credits or you don\'t have enough rights to access it.')
        if response.status_code==500:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Zenscrape Error! Internal Server Error.')
        else:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Zenscrpae Error! Request failed')
    except Exception as e:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] {e}')

    return None


#Using zenscrape API
def scraperapi(url):
    current_date = datetime.datetime.now()
    
    #Getting api key from key.json file
    api_key = get_key('scraperapi')

    #returning none if no key found
    if not api_key:
        return None

    #parmeters for request
    params = (
    ("url",url),
    ("api_key",api_key)
    );

    try:
        #preareing three requests at max if the request fails

        for tries in range (1,4):
            response = requests.get('https://api.scraperapi.com', params=params);


            if response.status_code==200:
                #returning the result if status code is 200 ok
                print(f'[{current_date.strftime("%H:%M:%S")}] [info] scraperapi request call successful.')
                
                return response.text
            print(f'[{current_date.strftime("%H:%M:%S")}] [info] Retrying API calls...')
            
            

        #printing error if status code is not 200
        if response.status_code==403:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Scraperapi Error! Forbidden -- API key is wrong, you don\'t have enough credits or you don\'t have enough rights to access it.')
        if response.status_code==500:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Scraperapi Error! Internal Server Error.')
        else:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Scraperapi Error! Request failed')
    except Exception as e:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] {e}')
    return None
    
    
#Using scrapingdog API
def scrapingdog(query):
    current_date = datetime.datetime.now()
    
    #getting api key from key.json file
    api_key = get_key('scrapingdog')
    if not api_key:
        return None


    #paramters for api request
    params = (
    ("query",query),
    ("results","100"),
    ("country","us"),
    ("api_key",api_key)
    );

    try:

        response = requests.get('https://api.scrapingdog.com/google', params=params);

        # print(response.text)
        links=[]
        #returning results as array if status code is 200
        if response.status_code==200:
            print(f'[{current_date.strftime("%H:%M:%S")}] [info] scrapingdog request call successful.')


            # print(type(response.text))
            response_data=json.loads(response.text)
            for data in response_data["organic_data"]:
                # print(data)
                links.append(data["link"])
                
            # print(links)

            return links
            
        #printing error when status code is not 200
        if response.status_code==403:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Scraperapi Error! Forbidden -- API key is wrong, you don\'t have enough credits or you don\'t have enough rights to access it.')
        if response.status_code==500:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Scraperapi Error! Internal Server Error or wrong API key.')
        else:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Scraperapi Request failed: Something went wrong or key is invalid')
    except Exception as e:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] {e}')
    return None
   

