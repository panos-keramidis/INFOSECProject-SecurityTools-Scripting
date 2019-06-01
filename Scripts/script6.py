# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 02:37:25 2019

@author: panos
"""

import os
import sys
import re
import crypt

os.system("passwd -l {sudo getent shadow | grep '^[^:]*:.\?:' | cut -d: -f1}")

#κάνει απενεργοποίηση όλους τους χρήστες που έχουν κενό password

#ψαχνει του κρυπτογραφημενους κωδικους στο shadow, ενα συγκεκριμένο regex  και συγκεκριμένο πεδίο
#με το passwd -l κλειδώνει τους χρηστες