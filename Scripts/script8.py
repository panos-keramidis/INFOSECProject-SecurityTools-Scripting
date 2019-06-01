# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 03:29:53 2019

@author: panos
"""



import os
import sys
import re
import crypt

os.system("find / -perm -4000 -exec ls -l {} \;")

#βρίσκει τους χρήστες με δικαίωμα 4000 που σημαίνει UID και επιστρέφει τα στοιχεία τους