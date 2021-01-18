# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:36:44 2021

@author: Charan C
"""


import urllib
import time
import winsound

url = "https://www.google.com/"

while True:
    
    try:
        result = urllib.request.urlopen(url).getcode()
           
        if result == 200:        
            print("Site is Up : {}".format(result))
            winsound.MessageBeep()
            time.sleep(1)
            
    except BaseException as e:
        print("Not able to fetch the Site details : {}".format(e))
        time.sleep(1)
