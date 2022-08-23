import os
import json
import datetime



def get_key(key):
    current_date = datetime.datetime.now()

    if not os.path.exists('./key.json'):
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] API Key file "key.json" doesnot exist')
        print(f'[{current_date.strftime("%H:%M:%S")}] [Warning] Terminating Program')
        quit()


    try:
        key_file= open('./key.json')
        key_data = json.load(key_file)

        # print(key_data[key])
        
        key_file.close()

        if key_data[key] == None:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Switching API..\n{key} key not found.')
            # return None

        return key_data[key]
    except:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Error in JSON file!')

# get_key('test')