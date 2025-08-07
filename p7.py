#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:26:02 2025

@author: root
"""

l=[1,2,3,4,5,6,7,8,9]

size = len(l)//3

l1 = (l[0:size])[::-1]
l2 = l[size:2*size][::-1]
l3 = l[2*size:3*size][::-1]
print(l1,l2,l3)
