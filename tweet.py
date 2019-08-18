import requests
import re
import os
import json
import sys
from colorama import init, Fore
init(autoreset=True)

files = sys.argv
filename = files[1] 


print("""
 _  _  _       _                        
| || || |     | |                       
| || || | ____| | ____ ___  ____   ____ 
| ||_|| |/ _  ) |/ ___) _ \\|    \\ / _  )
| |___| ( (/ /| ( (__| |_| | | | ( (/ / 
 \\______|\\____)_|\\____)___/|_|_|_|\\____)                                  
""")

print("=================================")
print("Twitter Valid E-Mail Checker V1.0")
print("=================================")

print("""
###############################################
###############################################
###### Developer: ᏕᎮᏋᏨᎨᎯᏝ ᏨᎧᏧᏋᖇ   #############
###### Telegram: @MuslimSoldier   #############
###### Github: @Promunim          #############
###### Copywrite  © 2019 @MuslimSoldier  ######
#### Stealing codes does't make you coder  ####
##### => Ethiopian Coders Association <= ######
############################################### 
""")

input("Press Any Key to Continue")

def checker(mail):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Save-Data': 'on',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0.0',
    'TE': 'Trailers',
    }

    params = (
    ('email', mail),
    )
    response = requests.get('https://api.twitter.com/i/users/email_available.json', headers=headers, params=params)
    msg = response.json()
    message = msg['msg']
    return message
    

#response = requests.get('https://api.twitter.com/i/users/email_available.json', headers=headers, params=params)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".


live = 0
died = 0
error = 0
lista = 1

if(filename != ""):
    file = open(filename,'r')
    contents = file.read()
    maillist = contents.split("\n")
    amount = len(maillist)
    find = "Email has already been taken."
    for mail in maillist:
       res = checker(mail)
       if find in res:
            print(lista,Fore.GREEN + "Live: " + mail)
            live = live + 1
            file = open("twitter_live.txt","w") 
            file.write(mail)
            file.close()
            lista = lista  + 1
       else:
            print(lista,Fore.RED + "Died: " + mail)
            died = died + 1
            lista = lista + 1

    print("+++++=>Twitter Check Result <++++++")
    print("Total Checked: %s" % amount)
    print("Total Live: %s" % live)
    print("Total Died: %s" % died)
    print("+++++=> ..END.. <=++++")
    print("++++=> Twitter Valid Email Checker V1.0 <=++++")   
    print("++++=> @MuslimSoldier Copywrite 2019 <=++++")    
    print("++++=> Global Coding Inc. <=++++")    
else:
     print(Fore.RED + "Empty File Name!")
     print(Fore.BLUE + " Usage python tweet.py filename.txt")
     print(Fore.BLUE + " Example: python tweet.py emails.txt")