#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:44:31 2025

@author: root
"""

l=[1,2,4,5,7,8,35,43,65,151,55,32,10]

for i in l:
    if(i > 150):
        break
    
    if(i%5 == 0):
        print(i)