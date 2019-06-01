# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:44:45 2019

@author: panos
"""

import os
import sys
import re
import crypt

choice = input("Enter Your choice (1. System Info 2. Uptime 3. Who is connected): ")  #παίρνουμε την επιλογή του χρήστη

#αντίστοχα πράττουμε

if choice == 1:
    os.system('hostnamectl')    #πληροφορίες συστήματος (OS, έκδοση, όνομα)
elif choice == 2:
    os.system('uptime') #χρόνος που είναι ενεργός
elif choice == 3:
    os.system('w')  #ποιοί είναι ενεργοί τώρα




