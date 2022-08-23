# Defascan: Defacement Scan and Alert
```
 ____        __                           
|  _ \  ___ / _| __ _ ___  ___ __ _ _ __  
| | | |/ _ \ |_ / _` / __|/ __/ _` | '_ \ 
| |_| |  __/  _| (_| \__ \ (_| (_| | | | |
|____/ \___|_|  \__,_|___/\___\__,_|_| |_|
```
Defascan is a python tool that will scrape the internet for your given google dork queries using APIs and alert using the email provied during rutime.

## Installation
`git clone https://github.com/test/test.git`

`pip install -r requirements.txt`

## Requirements
Choose at least one of the given APIs for the program to run smoothly.
- [Scrapper API](https://www.scraperapi.com/)
- [Zenscrape API](https://zenscrape.com/)
- [Scrapingdog API](https://www.scrapingdog.com/)

Register using your email to get the API tokens. Place the token in key,json file in the same directory.
##### (Note: Free tier regiestration given you enough credit per month to easily run the program.)

## Usage
```
python3 main.py -h 

usage: main.py [-h] [--min MIN] [--max MAX] [--sender SENDER_MAIL] [--admin ADMIN_MAIL] [--pass SENDER_PASS] [--perm]
               [--query QUERY] [-n NUMBER_OF_PAGES]

DefaScan: Defacement Scanner and Alert

optional arguments:
  -h, --help            show this help message and exit
  --min MIN             Minimum delay (in seconds) between a Google dork search. Default: 37 (default: 37)
  --max MAX             Maximum delay (in seconds) between a Google dork search. Default: 60 (default: 60)
  --sender SENDER_MAIL  Sender's email (default: None)
  --admin ADMIN_MAIL    Admin's email you want to send the scan report to (default: None)
  --pass SENDER_PASS    Sender's password for email (default: None)
  --perm, -p            Permission to run scanner without APIs. (default: False)
  --query QUERY, -q QUERY
                        query search for Google dork (default: site:.np intitle:"hacked by")
  -n NUMBER_OF_PAGES    number of search queries for scraping (default: 1)
```

## Usage
Go to the direcotry containing main.py and run:

`➜ /bin/python3 main.py --min 50 --max 60 -p -n 10 --sender sender@senermail.com --admin 
admin@adminmail.com --pass senderpass `

### key.json
This file should hold the API keys obtained after the registration.
```
{
	"scraperapi": "YourKeyHere",
	"scrapingdog": "YourKeyHere",
	"zenscrape": "Your-Key-Here"

}

```

### subscriber.json
This file should contain the information regarding the organization including their name, urls to check and email to contact.
```
{
	"Data": [
		{
			"suscriberID": 1,
			"name": "organization.com.np",
			"url": [
				"organization1.com.np/cwne.html",
				"organization1.com.np/a.html"
			],
			"email": "contact@mail.com"
		},
		{
			"suscriberID": 2,
			"name": "org2.edu.np",
			"url": ["org2.edu.np/site"],
			"email": "org2@contact.com"
		}
    ]
}
```
### exclude.json
This file should contain the urls of the site that we donot wish to contact at all.
```
{
	"Data": [
		{
			"url": "http://organization.com.np/no"
		},
		{
			"url": "http://abcd.com"
		}
	]
}

```

### Record folder
Record folder will how all the output including the htmls and pdfs generated durint the scan.
