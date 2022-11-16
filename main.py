from os import link
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from generate_report import *
from link_handler import get_uniq
from noapi import *
import re
import datetime
from check_susbcriber import check_subscriber

# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
from screenshot import take_screenshot
from api import scrapingdog, zenscrape, scraperapi
from parse_argument import parse_args
from send_email import send_gmail
from cleanup import cleanup
from subscriber_scan import scan_link
from zip import zip_file

def main(args):

    print(" ____        __                           ")
    print("|  _ \  ___ / _| __ _ ___  ___ __ _ _ __  ")
    print("| | | |/ _ \ |_ / _` / __|/ __/ _` | '_ \ ")
    print("| |_| |  __/  _| (_| \__ \ (_| (_| | | | |")
    print("|____/ \___|_|  \__,_|___/\___\__,_|_| |_|\n")
                                           



    #storing date for terminal message
    current_date = datetime.datetime.now()

    #storing user input
    sender_mail=args.sender_mail
    sender_pass=args.sender_pass
    admin_mail=args.admin_mail
    query = args.query


    links = [] ## Initiate empty list to capture final results

    ## Specify number of pages on google search, each page contains 10 #links
    n_pages = int(args.number_of_pages)

    #intializing parsed html file
    soup=""
    for page in range(0, n_pages):
        #use of api links
        url ="https://www.google.com/search?q=" + query + "&start=" + str(page * 10)

        
        #Using APIs for sending request
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Using ScrapperAPI")
        scraper_request=scraperapi(url)

        #Parsing response to html using beautiful soup
        if scraper_request:
            soup = BeautifulSoup(scraper_request, 'html.parser')
        else:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Using ZenscrapeAPI")

            #Using zenscrape API
            zenscrape_request=zenscrape(url)
            if zenscrape_request:
                soup = BeautifulSoup(zenscrape_request, 'html.parser')
            else:
                #Using Scrappingdog APi
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Using ScrapingdogAPI")

                result=scrapingdog(query)

                if result:
                    for url in result:
                        links.append(url)
                    soup = "scrapingdog"
                

        ## soup = BeautifulSoup(r.text, 'html.parser')

        #triggered when all API request fails
        if not soup:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [WARNING] All API requests failed.\n Do You want to continue without using any API. It might cause ip block from google!")
            print(args.noapi_permission)
                
            #asking for permission if permission not specified user in switch 
            if args.negative_noapi_permission:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [ERROR] Permission not given. Terminating Program!")

                quit()

            if not args.noapi_permission:
                permisson = input("Y/N:  ")
                if permisson=='y' or permisson=="Y":
                    args.noapi_permission=True
                else:
                    #terminating program if permission is not given
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [ERROR] Terminating Program!")
                    quit()
            
            #proceeding without using any apis
            noapi_request = noapi(url,args.min,args.max)
            soup = BeautifulSoup(noapi_request, 'html.parser')


            #quiting program when direct reqeust also fails
            if not soup:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [WARNING] All Requests failed! API misconfiguration and IP blocked by google. Terminating Program.")
                quit()

            
        # print(soup)

        #pulling out page links from parsed html
        if soup!="scrapingdog":
            search = soup.find_all('div', class_="yuRUbf")

        
                
            if search:

                #appending links to main list

                for h in search:
                    links.append(h.a.get('href'))
            else:

                #pulling out page links from parsed html

            
                search2 = soup.find_all('div', class_="egMi0")
                if search2:
                    for h in search2:
                        res=h.a.get('href')
                        url= re.search('(?<=url\?q=)(.*)(?=&sa=)',res)
                        # print("search2:", url.group())
                        links.append(url.group())
                
                else:
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] \nQuery Finsihed\n")
                    break

    #printing out scrapped url
    print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Scrapped urls:")


    #writing the url in a text ifle
    f = open("list.txt", "w")

    for url in links:
        print(url)
        f.write(url+'\n')
    
    f.close()


    #filtiring urls
    handled_link=get_uniq(links)
    #taking screenshots of the image
    print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Taking Screenshots")

    data_for_template = take_screenshot(handled_link)

    #generating webpage using the links and images
    print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Generating PDF")

    data_for_pdf = generate_webpage(data_for_template)

    #generating pdf version of the webpage
    generate_pdf(data_for_pdf)

    print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] [INFO] Creating zip file')

    zip_file()

    #sendimg report to admin as gmail
    #send_gmail(sender,reciever,sender_pass)

    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Sending mail to admin")
    if (sender_mail!= None and admin_mail!=None and sender_pass!=None):
        send_gmail(sender_mail,admin_mail,sender_pass)
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Main mail sent successfully")
    else:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [ERROR] Mail sent fail Sender or Admin Mail or credential Missing. Use -h for help.")

    


    #Scanning for affected user from our subscriber list
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Scanning from Susbscriber")
    affected_user=scan_link()
    if affected_user:
        #taking screenshots of the image
        li=[]
        for l in affected_user:
            li.append(l['url'])
        
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Generating report for Susbscriber")

        data_for_template = take_screenshot(li)
        i=0

        for data in data_for_template:
          #generating webpage using the links and images
            data_for_pdf = generate_webpage(data,indiv=True)

            #generating pdf version of the webpage
            generate_pdf(data_for_pdf)
            # print(affected_user[i]["word"])

            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Sending Mail to subscriber")

            send_gmail(sender_mail,affected_user[i]["email"],sender_pass,scan=[data,affected_user[i]["word"]])
            i+=1
    # quit()


    #Checking if the affected urls are in our subscriber list to send mail
    subscribers= check_subscriber(handled_link)

    if subscribers:
        for subinfo in subscribers:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Generating report for Susbscriber")

            #generating webpage using the links and images
            data_for_pdf = generate_webpage(subinfo,indiv=True)

            #generating pdf version of the webpage
            generate_pdf(data_for_pdf,True)
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Sending Mail to subscriber")

            send_gmail(sender_mail,subinfo["email"],sender_pass,indiv=subinfo)

    #cleaning up the project file at the end
    cleanup()





if __name__=="__main__":
    #taking the arguments passed by the user
    arguments=parse_args()
    main(arguments)
