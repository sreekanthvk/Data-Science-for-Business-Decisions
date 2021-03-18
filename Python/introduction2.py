# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:53:03 2021

@author: Sreekanth V K
"""

'''
Comments

dsfdf
sdf

sdf

'''

"""
Comments
asfdf
dfdf

"""
import pandas as pd
from pandas import read_csv
from matplotlib import plot as plt 


num1 = 2
num2 = 3
num3 = num1 + num2

if (num1 >1 ):
    print("greater")
else:
    print("not greater")
    
for i in range(1,10):
    print(i)
    

# in R, fun <- function(Arg) {}

def function_name(arg1, arg2):
    return (arg1 + arg2)

function_name(1,3)



# Write a function compare_input ( arg1)
# if arg1 > 0 it should print "Positive" , <0, negative and otherwise it should print zero
# compare_input(-1)
# compare_input(1)
# compare_input(0)

def compare_input(arg1):
    if(arg1>0):
        return("Positive")
    elif(arg1<0):
        return("Negative")
    else:
        return("Zero")

compare_input(-1)


new_list = [1,2,3,4]

new_list[1]

dictionary = {"k1":"v1", "k2": "v2"}
dictionary["k1"]
dictionary["k3"] = "v3"
dictionary["k1"] = "v10"


sample_data = pd.read_csv("D:\\Learning\\Statistical Analysis Using R\\data\sample.csv")
sample_data[sample_data["Y"] < 1] ["X1"]




















    
