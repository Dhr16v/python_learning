#Modules and Packages

#Modules are files containing Python code (functions, classes, etc.).

# What is a Module?

# A module is simply a Python file (.py) that contains functions, variables, and classes.
# You can import and reuse it in other programs.

import math

print('pi:',math.pi)
print('square root of 16:',math.sqrt(16))
print('factorial of 5:',math.factorial(5))
print('sin of 30:',math.sin(30))
print('cos of 30:',math.cos(30))
print('tan of 30:',math.tan(30))
print('log of 10:',math.log(10))
print('log10 of 10:',math.log10(10))
print('log2 of 10:',math.log2(10))
print('exp of 1:',math.exp(1))
print('pow of 2,3:',math.pow(2,3))
print('ceil of 3.1:',math.ceil(3.1))
print('floor of 3.9:',math.floor(3.9))

#random module
import random

print('random number:',random.random())
print('random integer:',random.randint(1,100))
print('random choice:',random.choice([1,2,3,4,5,6,7,8,9,10]))

#datetime module
import datetime

today=datetime.date.today()
print('today:',today)

current_time=datetime.datetime.now()
print('current time:',current_time)

print('year:',current_time.year)
print('month:',current_time.month)
print('day:',current_time.day)

#os module

import os

print('current working directory:',os.getcwd())
print('list of files and directories:',os.listdir())

#sys module
import sys
print('system platform:',sys.platform)
print('system version:',sys.version)
print('system path:',sys.path)
print('system argv:',sys.argv)
print('system exit:',sys.exit())
print('system maxsize:',sys.maxsize)
print('system maxunicode:',sys.maxunicode)
print('system maxfloat:',sys.maxfloat)
print('system maxint:',sys.maxint)
print('system maxlong:',sys.maxlong)
print('system maxlonglong:',sys.maxlonglong)

