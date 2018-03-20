import schedule
import time


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

#Let the user choose the timeframe for an information cycle
choose_start = input("When do you want to start your distraction free day? (Please use XX:YY format)")
choose_end = input("When do you want to end your distraction free day? (Please use XX:YY format)")


###Turn on the blocker
def turn_on():
    with open(hosts_path,'r+') as file:
        content=file.read()
        print(content)

        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect+" "+website+"\n")
                if website.startswith('www.'): #We're adding www where needed
                    temp = website.split('www.')[1]
                    file.write(redirect+" " + temp + "\n")
                else:
                    file.write(redirect+" " + "www." + website + "\n")
                print("Blocked website")
###Turn off the blocker
def turn_off():
    print("Unblocking everything")
    with open(hosts_path,'r+')as file:
        content=file.readlines()
        file.seek(0) #Starts reading at the first character
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate() #Imame golqm problem s mahaneto na failove ot hosts - maha samo chast ot tqh
    print("Unblocked everything")

#Schedule the turn on and off of the blocker as defined by user
schedule.every().day.at(choose_start).do(turn_on)
schedule.every().day.at(choose_end).do(turn_off)

while True:
    schedule.run_pending()
    time.sleep(1)
