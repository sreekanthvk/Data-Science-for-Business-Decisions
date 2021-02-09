# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math 
from math import pow,sqrt

variable1 = 2
variable2 = 3
variable3 = variable1 + variable2
variable3

variable1 = "Hello"
variable2 = " World"
variable3 = variable1 + variable2
variable3

lst = []
dct = {}

lst.append(1)
dct["Student1"] = "Name1"
dct["Student2"] = "Name2"

dct["Student1"] = {"Name": "Sreekanth", "Code": "F1", "Department": "SOMS", "PIN": 673601}
dct["Student2"] = {"Name": "Sreekanth2", "Code": "F2", "Department": "SOMS", "PIN": 673601}
dct["Student2"] = {"Name": "Sreekanth3", "Code": "F2", "Department": "SOMS", "PIN": 673601}

sum([variable1,variable2])

sqrt(100)
math.pow(variable1,variable2)
pow(variable1,variable2)

array = np.array([1, 2, 3])
np.mean(array)
np.mean(lst)
array.mean()
lst.mean()

def sum_of_variables (var1, var2):
    # var1 + var2
    return(var1+var2)

sum_of_variables(1,2)


if (2 == 2):
    print("Equal")
else:
    print("Else")
    print("Not Equal")


for key in dct:
    print(dct[key])
