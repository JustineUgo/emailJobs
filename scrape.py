import requests
from bs4 import BeautifulSoup

"""
Scrapes freelancing websites for jobs :upwork.com,peopeleperhour.com,freelance.com
"""

class Scrape:
    
    #header for permission
    header ={"User-Agent": "Mozilla/5.0"}
    def __init__(self, technology):
        self.technology = technology
    
    def upwork(self):
        
        #connect to upwork
        url = "https://www.upwork.com/search/jobs/?q={}&sort=recency".format(self.technology)
        upwork_web = requests.get(url, headers=Scrape.header)
        
        #extract job offer and time
        soup = BeautifulSoup(upwork_web.content, 'html.parser')
        jobs = soup.find_all("up-c-line-clamp")
        time = soup.find_all("time")
        
        #construct a job and put in message for mail
        message=""
        for position in range(10):
            job_title=jobs[position].get_text()+ "\n"
            date_of_posting_job = str(time[position])[24:34]+", "
            time_of_posting_job = str(time[position])[35:43]+"\n"
            
            a_job = job_title+date_of_posting_job+time_of_posting_job
            
            message+=a_job+"\n"
        with open("message.txt", "w") as f:
            f.write(message)
            
            
#Scrape("python").upwork()
        


