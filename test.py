
import smtplib
 
# creates SMTP session
s = smtplib.SMTP_SSL('smtp.titan.email', 465)
 
# start TLS for security
 
# Authentication
s.login("ayush@madu.ninja", "TesT7410!!")
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail("ayush@madu.ninja", "shyambahadurxhrextha@gmail.com", message)
 
# terminating the session
s.quit()