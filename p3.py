#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:06:01 2025

@author: root
"""

str=input("Enter string :")

for i in range(0,str.__len__()-1):
    if(i==0): continue
    if(i % 2 == 0):
        print(str[i],i)