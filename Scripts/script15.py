# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:34:36 2019

@author: panos
"""


import os
import sys
import re
import crypt

#Το script αυτό σκοτώνει έπειτα από εντολή διαχειριστή όλες τις διεργασιές που καταναλώνουν ύποπτα υψηλή μνήμη

os.system("ps aux --sort=-%mem | awk 'NR<=5{print $0}'")    #επιστρέφει τις 5 πιο κοστοβόρες από άποψη μνήμης διεργασίες


pids = raw_input("Enter the PID(s) of the processes that look suspicious: ")  #ζηταμε από τον χρήστη να επιλέξει pid

os.system("kill " + pids)  #σκοτώνουμε τη διεργασία
