import json
import re
import os
import datetime

def check_subscriber(data):
    current_date = datetime.datetime.now()

    #chekcing if the subscriber.json file exists
    if not os.path.exists('./subscriber.json'):
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Subscriber file "subscriber.json" doesnot exist')
        # quit()


    try:
        #loading data from subscriber.json file
        subscriber_file= open('./subscriber.json')
        subscriber_data = json.load(subscriber_file)

        # print(key_data[key])
        
        subscriber_file.close()
    except Exception as e:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Error in Subscriber file')
        print("\ne")

    # print(subscriber_data)

    #initializing empty array to store affected users
    affected_subscriber=[]

    for link in data:
        #using regex to take out name from the url
        link_search= re.search('(?<=:\/\/)(.*)(.np)',link)
        linkname=link_search.group()

        for subscriber in subscriber_data["Data"]:
            #appending data of user to affaected_subscriber
            if subscriber["name"] in linkname:
                subscriber["link"]=link
                affected_subscriber.append(subscriber)


    return affected_subscriber

    






