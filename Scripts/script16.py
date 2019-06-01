# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:50:35 2019

@author: panos
"""

import os
import sys
import re
import crypt

#Το script αυτό ελέγχει ποιές υπηρεσίες ξεκίνησαν στο boot του server και δινει τη δυνατότητα να τις διαγράψει ο χρήστης
#sudo apt-get install systemd


os.system('systemctl list-units --type service')    #επμφανίζουμε τις υπηρεσίες που ξεκίνησαν από το bootstart

service = raw_input("Enter Your service that you want to end: ")  #ζητάμε ποια υπηρεσία θέλει ο χρήστης να σταματήσει

os.system('sudo systemctl disable ' + service)    #και την απενεργοποιούμε
