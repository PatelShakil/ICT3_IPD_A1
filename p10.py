#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:36:59 2025

@author: root
"""

size=int(input("Enter size:"))
for i in range(1,size + 1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()