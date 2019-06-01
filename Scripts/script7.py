# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 03:28:57 2019

@author: panos
"""



import os
import sys
import re
import crypt

os.system("grep '^sudo:.*$' /etc/group | cut -d: -f4")
#ψάχνει τους χρήστες που είναι sudo (διαχειριστές) στο group file και εμφανίζει το ονομα τους