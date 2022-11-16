# Python code to illustrate Sending mail with attachments
# from your Gmail account 
  
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

   
def send_gmail(sender,reciever,sender_pass,scan=False,indiv=False):
  
    
    # instance of MIMEMultipart
    message = MIMEMultipart()
    
    # storing the senders email address  
    message['From'] = sender
    
    # storing the receivers email address 
    message['To'] = reciever
    
    # storing the subject 
    message['Subject'] = "Defascan report"

    if scan:
        body=f"Dear Sir/Madam,\nA report generated by our program has found out your site under our monitor to possibly compromised. It contains word '{scan[1]}' flagged by our program. We have attached a image of the page that might have been affected. We have sent this email because you were subscribed to our program. "

        files=[f"html_single_report_{scan[0]['name']}.html.pdf"]

    elif indiv:
        body=f"Dear Sir/Madam,\nA report generated by our program has found out your site under our monitor to be compromised. We have attached a image of the page that might have been affected. We have sent this email because you were subscribed to our program. "
        
        files=[f"html_single_report_{indiv['name']}.html.pdf"]
    else:
        body = "Dear Sir/madam\n The given is the Defascan generated report. It contains the result of the scan performed at this given time."
        files=["html_report.html.pdf","html.zip"]

    # string to store the body of the mail
    
    # attach the body with the message instance
    message.attach(MIMEText(body, 'plain'))
    
    # open the file to be sent 


    for file in files:
        # filename = "html_report_jinja.html.pdf"
        attachment = open(f"./{file}", "rb")
        
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        
        # encode into base64
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % file)
        
        # attach the instance 'p' to instance 'message'
        message.attach(p)
    

    try:
        # creates SMTP session
        smtp_session = smtplib.SMTP_SSL('smtp.titan.email', 465)
        
        
        # start TLS for security
        # smtp_session.starttls()
        
        # Converts the Multipart message into a string
        text = message.as_string()
        
        # Authentication
        smtp_session.login(sender, sender_pass)
        
        
        
        # sending the mail
        smtp_session.sendmail(sender, reciever, text)
    
        # terminating the session
        smtp_session.quit()
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Mail Sent Successfully")

    except Exception as e:
        print(e)
        



# a=[{'suscriberID': 1, 'name': 'nationallife.com.np', 'email': 'nationallife@gmail.com', 'link': 'https://nationallife.com.np/cwne.html'}, {'suscriberID': 2, 'name': 'mercy.edu.np', 'email': 'nationallife@gmail.com', 'link': 'https://www.mercy.edu.np/site/'}, {'suscriberID': 3, 'name': 'bnkschool.edu.np', 'email': 'nationallife@gmail.com', 'link': 'https://bnkschool.edu.np/about/'}]
# send_gmail('033b8041c28dcb','laxmanbahadurxhrextha@gmail.com','e41da95ecdaf98')

# send_gmail('ayush@madu.ninja','haribahadurxhrextha@gmail.com','TesT7410!!')
