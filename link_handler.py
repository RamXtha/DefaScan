import datetime
import json
import os


#filter out urls
def get_uniq(url_list):


    #selecting only unique urls
    set_list=set(url_list)

    unique_list=(list(set_list))

    #checking for exclude.json file
    if not os.path.exists('./exclude.json'):
        print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] [WARNING] Exclude file "exclude.json" doesnot exist')
        return unique_list


    try:
        exclude_file= open('./exclude.json')
        exclude_data = json.load(exclude_file)

        
        exclude_file.close()
    except Exception as e:
        print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] [Error] Error in Subscriber file')
        print("\ne")
    
  
    #removint urls present in exclude.json file
    for link in unique_list:
        for exlcude_link in exclude_data["Data"]:
            if link in exlcude_link["url"]:
                # print("link excluded.")
                unique_list.pop(unique_list.index(link))
                
    return unique_list
    # print(unique_list)




