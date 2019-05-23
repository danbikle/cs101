# coding: utf-8
"""
py4ds1.py

This is a simple script used for training people new to Python.
"""

# ## Python for Data Science
# ### Learning Center V0.9
# ### Date: 20Jan2018

print("Hello, Python!")


# ### --- Exercise 1
# ### Print the following string "Learning Python for Data Science"

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)

a = b = c = 1
print(a)
print(b)
print(c)


# ### --- Exrecise 2
# ### Create variables with your first_name and last_name
# ### print first_name and last_name

first_name = "Learning"
last_name = "Center"
print(first_name)
print(last_name)
print(first_name," is ",last_name)

str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + " " + "TEST") # Prints concatenated string


# ### --- Exercise 3 
# ### print first two characters of first_name and last two characters of last_name

first_name = "Learning"
last_name = "Center"
print(first_name[0:2])
print(last_name[-2:])


###########################################################
## Python Lists
###########################################################
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]

print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd 




###########################################################
## Python Tuples
###########################################################
tuple = ('abcd', 786 , 2.23, 'john', 70.2 )

print(tuple)          # Prints complete list
print(tuple[0])       # Prints first element of the list
print(tuple[1:3])     # Prints elements starting from 2nd till 3rd 

## Decisions in Python
var = 100
if var == 2000:
   print("1 - Got a true expression value")
   print(var)
elif var == 150:
   print("2 - Got a true expression value")
   print(var)
elif var == 100:
   print("3 - Got a true expression value")
   print(var)
else:
   print("4 - Got a false expression value")
   print(var)

## For and while Loops
## while loop
count = 9
while (count > 0):
   print('The count is:', count)
   count = count - 1

## for loop
for letter in 'Python':     # First Example
   print('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print('Current fruit :', fruit)

## Regular expressions
import re

line = "Cats are smarter than dogs"

## Matching using re
matchObj = re.match(r'(.*) are (.*)',line,re.M|re.I)

print(matchObj.group(1))
print(matchObj.group(2))

## search and replace
phone = "2004-959-559 # This is Phone Number"

# make 2004 to be 4002
num = re.sub(r'2004',"4002", phone)    
print("Phone Num : ", num)

## Functions in Python
def add_numbers(a,b):
    c = a + b
    return c

result = add_numbers(2,3)
print(result)

for x in range(10):
    print(x)

## Pass list as function argument
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])

## Appending and extending Python lists
list1 = [1,11,111]
list2 = [2,22,222]

list1.append(1111)
print("list1-a = %s" % list1)

list1.extend(list2)
print("list1-b = %s" % list1)

## Integer and floating division
def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))
    
def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y)) # integer division

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

# Printing list length
list = ['a', 'b', 'c', 'd', 'e']
print(len(list))

# Splitting strings
ss = "This is Sunnyvale This is Cupertino"

words = ss.split()
print(words)
d = {}.fromkeys(words,0)
for w in words:
    d[w] += 1
print(d)

