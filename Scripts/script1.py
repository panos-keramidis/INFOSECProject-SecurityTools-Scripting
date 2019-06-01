# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:15:13 2019

@author: panos
"""

import os
import sys
import re
import crypt

#Το script αυτό δημιουργεί έναν νέο χρήστη αναλόγως με το τι θα του υποδείξει ο χρήστης

username = raw_input("Enter Your Username: ")  #παίρνουμε το όνομα του χρήστη

password = raw_input("Enter Your Password: ")  #παίρνουμε το συνθηματικό του χρήστη

while True: #κάνει τους ελέγχους που υποδεικνύονται
    if len(password) < 6:
        os.system('echo "Give at least 6 digits"')
    elif re.search('[0-9]',password) is None:
        os.system('echo "Give at least 1 number"')
    elif re.search('[a-z]', password) is None:
        os.system('echo "Give at least 1 small letter"')
    elif re.search('[A-Z]',password) is None: 
        os.system('echo "Give at least 1 capital letter"')
    elif re.search('[!@#$%^&*]',password) is None: 
        os.system('echo "Give at least 1 symbol"')
    else:
        os.system('echo "Your password is ok"')
        break


encpassword = crypt.crypt(password, "22")   #κρυπτογραφεί τον κωδικό

description = raw_input("Enter Your Description: ")  #παίρνουμε την περιγραφή του χρήστη

group = raw_input("Enter Your Group: ")  #παίρνουμε το group του χρήστη

os.system('sudo useradd -m -d /home/' + username + ' -g '+ group + ' -c'+ description + ' -p' + encpassword + ' ' + username)

#τέλος κάνει τον νέο χρήστη