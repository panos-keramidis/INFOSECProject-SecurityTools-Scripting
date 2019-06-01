# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 01:22:44 2019

@author: panos
"""

import os
import sys
import re
import crypt

#Το συγκεκριμένο script εμφανίζει το πλήθος των αποτυχημένων ενεργειών βάση ημερομηνίας

date = raw_input("Enter Your time period: ")  #τη διαβάζει

os.system('cat /var/log/secure | grep ' + date + ' | grep failure') #στο αρχείο των logs επιστρέφει 
#όλες τις προσπάθειες που είναι αποτυχημένες βάσει της συγκεκριμένης ημερομηνίας


os.system('cat /var/log/secure | grep root')    #στο ίδιο αρχείο επιστρέφει όλες τις προσπάθειες ως διαχειριστή



