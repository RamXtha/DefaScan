import json
import os
import requests

import urllib3
import datetime
#disable http only warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scan_link():
    #initalize empty affected array
    affected_users=[]

    #check for subscriber.json file
    if not os.path.exists('./subscriber.json'):
        print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] [Error] Subscriber file "subscriber.json" doesnot exist')
        # quit()


    try:
        subscriber_file= open('./subscriber.json')
        subscriber_data = json.load(subscriber_file)

        # print(key_data[key])
        
        subscriber_file.close()
        for data in subscriber_data["Data"]:

                #extracting url from file
                durl=data["url"]
               
                for url in durl:
                    # three tries
                    for tries in range (1,4):
                        try:
                            #sending request to client url
                            response = requests.get(f'http://{url}',verify=False);
                            
                            if response.status_code==200: 
                                # checking the page for harmful worlds
                                harmful= check_harmful(url,response.text)
                                if harmful:
                                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Harmful word {harmful}")
                                    #appending data to affected_users array
                                    harmful['email']=data['email']
                                    affected_users.append(harmful)

                                break
                            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Retrying.....")

                        except Exception as e:

                              print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [Error] URL error")
    
                        return list(affected_users)



    except Exception as e:
        print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] [Error] Error in Subscriber file')
        print("\ne")


    
            


#flagged words
bad=["hacked by","pwned by","defaced by"]

def check_harmful(url,data):
    #iterating harmful words over reponse text
    for words in bad:
        if words in data.lower():
            # print(words)
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Harmful word alert")

            return {"url":f"http://{url}","word":words}
            

