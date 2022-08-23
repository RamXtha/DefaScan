
import time
from jinja2 import Environment, FileSystemLoader

# import pdfkit
import os
from selenium import webdriver
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
import datetime



def generate_webpage(data,indiv=False):

    current_date = datetime.datetime.now()

    #Creating template environment
    env = Environment(loader=FileSystemLoader('templates'))


    #checking for type of html page to render
    if indiv:
        #Loading the template from the Environment

        template=env.get_template('single_page_template.html')
        page=f'html_single_report_{data["name"]}.html'

    else:

        template = env.get_template('report_template.html')
        page='html_report.html'




    #Rendering html page

    html= template.render(data=data,date=current_date)

    #Creating the HTML file
    with open(page, 'w') as f:
        f.write(html)
    
    return page



a=[{'url': 'https://nationallife.com.np/cwne.html', 'image': 'nationallife.com.np.png'}, {'url': 'https://www.ace.edu.np/noname.html', 'image': 'www.ace.edu.np.png'}, {'url': 'http://preranaktm.org.np/root.html', 'image': 'preranaktm.org.np.png'}, {'url': 'http://www.shreeramcharitra.edu.np/admin/assets/files/kingskrupellos.pdf', 'image': 'www.shreeramcharitra.edu.np.png'}, {'url': 'http://kathmandupost.ekantipur.com.np/news/2015-01-26/malaysia-air-site-hacked-by-group-claiming-support-for-is.html', 'image': 'kathmandupost.ekantipur.com.np.png'}, {'url': 'https://www.nbiit.edu.np/p/sel/bdedefi94eFjrv/13594617643858510.clc?page=notice&newsid=1', 'image': 'www.nbiit.edu.np.png'}, {'url': 'http://antardristi.com.np/r00t.html', 'image': 'antardristi.com.np.png'}, {'url': 'http://mounteverestbeni.edu.np/?page_id=136', 'image': 'mounteverestbeni.edu.np.png'}, {'url': 'https://www.mercy.edu.np/site/', 'image': 'www.mercy.edu.np.png'}, {'url': 'http://www.csj.org.np/current-and-future-work/', 'image': 'www.csj.org.np.png'}, {'url': 'http://www.csj.org.np/current-and-future-work/', 'image': 'www.csj.org.np.png'}, {'url': 'https://admin.mddohs.gov.np/2k22.html', 'image': 'admin.mddohs.gov.np.png'}, {'url': 'https://bnkschool.edu.np/about/', 'image': 'bnkschool.edu.np.png'}, {'url': 'https://sainomultimedia.com.np/2021/09/07/', 'image': 'sainomultimedia.com.np.png'}, {'url': 'http://www.imagegraphic.com.np/', 'image': 'www.imagegraphic.com.np.png'}, {'url': 'http://kath.gov.np/search_result?filter_name=%20Hacked%20By%20SN!P3R', 'image': 'kath.gov.np.png'}, {'url': 'https://sambasonuconstruction.com.np/', 'image': 'sambasonuconstruction.com.np.png'}]


def generate_pdf(page,indiv=False):
    #checking for type of report to make

    if indiv:
        print("generating single pdf")

        settings = {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
            "isHeaderFooterEnabled": False,
            "isLandscapeEnabled": True,
            "mediaSize": {
                # "height_microns": 210000,
                "name": "ISO_A5",
                "width_microns": 148000,
            },  
            "isCssBackgroundEnabled": True
        }
    else:
         settings = {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
            "isHeaderFooterEnabled": False,
            "mediaSize": {
                # "height_microns": 210000,
                "name": "ISO_A5",
                "width_microns": 148000,
            },  
            "isCssBackgroundEnabled": True
        }



    # using chrome driver to change html page to PDF file
    chrome_options.add_argument('--enable-print-browser')

    # taking directory to save file
    save_dir = os.getcwd()
    prefs = {
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        'savefile.default_directory': save_dir
    }
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),options=chrome_options)

    #savinf pdf using print in javascript
    driver.get(f'file://{save_dir}/{page}')
    time.sleep(1)
    driver.execute_script('window.print();')
    driver.close()
    
