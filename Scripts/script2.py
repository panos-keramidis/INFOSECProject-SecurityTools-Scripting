# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:23:55 2019

@author: panos
"""

import os
import sys
import re
import crypt

#το συγκεκριμένο script διαβάζει μια λέξη και εμφανίζει το ιστορικό των εντολών που την περιέχουν

word = raw_input("Enter Your word: ")  #τη διαβάζει

os.system("history | grep '" + word + "'")    #εμφανιζει όλα τα στοιχεία του ιστορικού των εντολών που την περιέχουν