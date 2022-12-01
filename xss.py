#!/usr/bin/env python
######## A-KENZI ########
####### XSS TRACK #######
## 7000+ BYPASS PAYLOAD ##
###### OPEN SOURCE ######
import sys
import requests
import threading
from colorama import Fore, Back, Style
import time


print(
        Fore.GREEN +
         """

███████████████████████████████████████████████████
█▄─▀─▄█─▄▄▄▄█─▄▄▄▄███─▄─▄─█▄─▄▄▀██▀▄─██─▄▄▄─█▄─█─▄█
██▀─▀██▄▄▄▄─█▄▄▄▄─█████─████─▄─▄██─▀─██─███▀██─▄▀██
▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
# PAYLOAD BYPASS XSS 2022
# Author Script : A-KENZI
# XSS Track 7000 Payload
        """ + Fore.RESET)

print()
file = open(sys.argv[1],'r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    time.sleep(0.15)
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'[ XSS Found ✓ ]','   ' , f"{url}" + Fore.RESET)
           print(Fore.GREEN , f"{url}" + Fore.RESET, file=open('hasil.txt','w'))
           #print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET, file=open('hasil.txt','a'))
        else:
           print(Fore.YELLOW +'[ XSS NOT Found ]','   ' , f"{url}" + Fore.RESET)

    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
