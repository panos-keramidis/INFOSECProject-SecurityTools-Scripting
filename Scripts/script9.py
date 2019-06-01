# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 03:43:04 2019

@author: panos
"""

import os
import sys
import re
import crypt
import netifaces as ni

#εφόσον έχουμε εγκαταστήσει nmap

ni.ifaddresses('enp0s3')
ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']  #παίρνουμε την ip μας


os.system("sudo nmap -sn " + ip + "/24")    #μέσω του nmap παίρνουμε για την ip μας τις πληροφορίες


