# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 03:37:34 2019

@author: panos
"""

import os
import sys
import re
import crypt


#υπάρχουν δυο τρόποι για απενεργοποίηση χρηστών μετά από 3 αποτυχημένες προσπάθειες εισόδου

#η πρώτη είναι να τροποποιήσουμε στα κάτωθεν δύο αρχεία τις δυό γραμμές 

#/etc/pam.d/system-auth and /etc/pam.d/password-auth
#auth        required      pam_faillock.so preauth silent audit deny=3 even_deny_root unlock_time=300
#auth        [default=die]  pam_faillock.so  authfail  audit  deny=3 even_deny_root unlock_time=300

#η δεύτερη είναι χειροκίνητα με την usermod

#usermod -L -e 1 {user}