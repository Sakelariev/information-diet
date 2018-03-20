
# coding: utf-8


## Website Blocker Code In Python
import time
from datetime import datetime as dt
hosts_temp="hosts"
hosts_path=r"/etc/hosts"
redirect="127.0.0.1"
website_list=[]
print("How many websites you want to block ???")
number=int(input())

while number!=0:
    print("Enter Website name !!")
    web=input()
    website_list.append(web)
    number -=1

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        print ("Working Hours... :) ")

        with open(hosts_path,'r+') as file:
            content=file.read()
            print(content)

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else :
        with open(hosts_path,'r+')as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print ("Happy Hours... :D ")

    time.sleep(300)
