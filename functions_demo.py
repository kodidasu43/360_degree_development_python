# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:07:03 2023

@author: LENOVO
"""
#import math


def additionofnumber(x,y):
  """This is a user function."""
  return x+y

def printtest():
    print("test")
    
my_lambda_function = lambda x,y: x+y

print(my_lambda_function(2,3))

print(additionofnumber(1000,2000))
printtest()

my_list = [1, 2, 3, 4, 5]

# Square each element of the list using a lambda function
squared_list = map(lambda x: x**2, my_list)
list_object = list(squared_list)

# Print the squared list
print(list_object)
