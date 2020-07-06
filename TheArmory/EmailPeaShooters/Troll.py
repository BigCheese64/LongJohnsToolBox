import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import configparser as cp
config = cp.ConfigParser()
config.read("EmailToEmailSpam.ini")
fromaddr=str(config['SETTINGS']['fromaddress'])
password=str(config['SETTINGS']['emailpassword'])
toaddr=str(config['SETTINGS']['targetaddress'])
subject=str(config['SETTINGS']['subject'])
body=str(config['SETTINGS']['body'])

l=0
while True:
    l=l+1
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
         
        msg.attach(MIMEText(body, 'plain'))
         
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print ('Email %s'%(l))
    except:
        if l<2:
            print("Did you allow access from less secure apps on the sender's email?")
        break
input("Press enter to quit.")
            


           
        
            

