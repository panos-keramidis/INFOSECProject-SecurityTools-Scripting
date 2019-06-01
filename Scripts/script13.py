# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:00:52 2019

@author: panos
"""

import os
import sys
import re
import crypt

#$ sudo apt install -y auditd audispd-plugins
#έχοντας εγκαταστήσει το auditd που είναι ένα χρήσιμο εργαλείο για monitor της ασφάλειας

date = raw_input("Enter Your Date: ")  #παίρνουμε μια ημερομηνία από τον χρήστη

os.system('aureport -ts' +  date + ' -te now --summary -i ')  #παράγει μια αναφορά βασει ημερομηνίας

#η αναφορά περιέχει τις μεταβολές δικαιωμάτων σε αρχεία