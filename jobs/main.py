import smtplib
from scrape import Scrape
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
"""
Sends email of jobs from upwork

"""

class EmailJobs:
    
    def __init__(self):
        #python email credentials and technology 
        self.technology = input("What technology, are you searching for? \n")
        self.gmail_user = input("What is the gmail address, python will use? \n")
        self.gmail_password = input("Type in the password: \n")

    def read_message(self):
        #quearies websites on a topic, puts output in message file and returns it for email structuring
        Scrape(self.technology).upwork()
        with open("message.txt", 'r', encoding='utf-8') as template_file:
            message_template = template_file.read()
        return message_template
    
    def send_mail(self, msg):
        
        # set up the SMTP server, login and send msg
        server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        server.login(self.gmail_user, self.gmail_password)
        
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Message successfully sent!")
        
        
    def main(self):
        #reads in message for body of email 
        body= self.read_message()

        #initialize complete message of mail and add the body of the message
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(body, 'plain'))
        
        # setup the parameters of the message: from, subject and to and then sends it
        msg['From']=self.gmail_user
        msg['Subject']="{} Jobs - Upwork".format(self.technology.title())
        with open("contacts.txt", 'r', encoding='utf-8') as receivers:
            for receiver in receivers:
                msg['To']=receiver
                self.send_mail(msg)
        del(msg)





EmailJobs().main()