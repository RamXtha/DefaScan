import datetime
import os
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#take screenshots from provided links
def take_screenshot(links):
    current_date = datetime.datetime.now()

    #opening browser in headless-mode
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),options=chrome_options)

    data_for_template=[]

    #Create picture folder if not exits
    if not os.path.exists('./pictures'):
        os.mkdir('./pictures')
        
    for url in links:
        try:
            # fetching the urls
            driver.get(url)
            driver.set_page_load_timeout(50)


                        #Check to see if alert exists in page
            try:
                while True:

                    alert = WebDriverWait(driver, 0.5).until(EC.alert_is_present())
                    
                    alert=driver.switch_to.alert;
                    print(alert.text)
                    alert.accept()

                    print(f'[{current_date.strftime("%H:%M:%S")}] [info] Alert Exists in page {url}')

                    if not alert:
                       break 

            except TimeoutException:
                pass

            filename= re.search('(?<=\/\/)(.*?)(?=\/)',url)
            f=filename.group()

            #collecting info for report
            webpage_info={}
            webpage_info["link"]=url
            webpage_info["name"]=f
            data_for_template.append(webpage_info)


            #saving screenshots in piture directory
            driver.save_screenshot(f'./pictures/{filename.group()}.png')
            print(f'[{current_date.strftime("%H:%M:%S")}] [info] Screenshot saved for {filename.group()}')

        except Exception as e:
            print(f'[{current_date.strftime("%H:%M:%S")}] [Error] {e}')
   

    return data_for_template


# a= ["https://www.arvisa.in/"]
# # 
# take_screenshot(a)