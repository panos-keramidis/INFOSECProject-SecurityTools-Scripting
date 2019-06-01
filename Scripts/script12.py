# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:57:10 2019

@author: panos
"""


import os
import sys
import re
import crypt

username = raw_input("Enter Your Username: ")  #παίρνουμε το όνομα του χρήστη

os.system('top -U ' + username)    #ελέγχουμε τις ενέργειες που έγιναν από αυτόν
