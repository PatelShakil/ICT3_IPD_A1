#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:19:37 2025

@author: root
"""

l1=[1,3,4,5,6]
el = l1[3]
l1.remove(el)

l1[1] = el
l1.append(el)
print(l1)
