# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:31:59 2019

@author: panos
"""

import os
import sys
import re
import crypt

#ρωταμε τον χρήστη ποια λειτουργία θέλει να επιλέξει

choice = input("Enter Your choice (1. Memory 2. Disk 3.CPU 4. All): ")  #παίρνουμε το όνομα του χρήστη

#αντίστοχα πράττουμε

if choice == 1:
    os.system("free -m")    #κατάσταση μνήμης
    os.system("free -m -b -n 1 > free.txt") #την γράφουμε και σε ένα απλό αρχείο
elif choice == 2:
    os.system("df")         #κατάσταση δίσκου
    os.system("df -b -n 1 > df.txt")    #την γράψουμε και σε ένα απλό αρχείο
elif choice == 3:
    os.system("top")        #κατάσταση CPU utilization 
    os.system("top -b -n 1 > top.txt")  #και σε αρχείο
elif choice == 4:
    os.system("free -m")        #όλα μαζί
    os.system("free -m -b -n 1 > free.txt")    
    os.system("df")
    os.system("df -b -n 1 > df.txt")
    os.system("top")
    os.system("top -b -n 1 > top.txt")
