import os
import datetime

from bleach import clean


def cleanup():
    current_date = datetime.datetime.now()

#making directory to store past files
    print(f'[{current_date.strftime("%H:%M:%S")}] [INFO] Cleaning up the Program folder')
    if not os.path.exists('record'):
        os.makedirs('./record')

    #preparing name for the folder
    folder_number = os.popen('ls ./record | wc -l').read()

    current_date = datetime.datetime.now()
    date=current_date.strftime("%Y_%d_%m-%H:%M:%S")

    folder_name= f"S{int(folder_number)+1}-{date}"

    #making folder for current scan
    if os.path.exists('html_report.html'):
        os.system(f'mkdir -p ./record/{folder_name}')


        #moving pdf and html file to the created file
        os.system(f"mv *.html *.pdf *.txt pictures ./record/{folder_name}")

# cleanup()