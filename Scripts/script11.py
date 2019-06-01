# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:09:43 2019

@author: panos
"""

import os
import sys
import re
import crypt

choice = input("Enter Your choice (1. Network 2. Processes): ")  #παίρνουμε την επιλογή του χρήστη

#αντίστοχα πράττουμε

if choice == 2:
    os.system('top')    #η κατάσταση διαδικασιών στον server
elif choice == 1:
    os.system('netstat')    #η κατάσταση δικτύου


