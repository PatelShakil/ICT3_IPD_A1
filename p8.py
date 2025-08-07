#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:29:15 2025

@author: root
"""

l=[1,2,3,2,3,32,7]
d={}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)