#            General and Mathematical Functions
#Functions in Python can be divided into two main categories: General Functions and Mathematical Functions.


#       GENERAL FUNCTIONS

#len
#Returns the number of elements in an object. If it is a string, it returns the number of characters.

#Example 1
y = len("python")
print(y)


#Example 2
x = len([1,2,3,4])
print(x)


#Format
x = format(3.457,".2f")
x = format(3.457,"08.2f")
y = format(3457,",")
t = format(57,"%")


#chr
#Returns the character that corresponds to a Unicode value.

x = chr(36)
print(x) # A


#ord
#Returns the Unicode code of a character.

x = ord("y")
print(x) # 121


#range
#Creates an iterable object that can iterate through the given start and end numbers.

x = list(range(10))
print(x)

y = list(range(1, 20, 3))
print(y)


#sum
#Returns the sum of all elements in a list, tuple or set.

x = sum ([1,2,3,4]) #list
print(x)
x = sum ((1,2,3,4)) #tuple
print(x)
x = sum ({1,2,3,4}) #set
print(x)

x = sum(range(1,10))
print(x)

sum([1, 5, 3])


#sorted
#Sorts an iterable object from smallest to largest. If the object contains string characters, it sorts according to the numerical equivalent of the character in the ASCII table.

x = sorted([4,5,-3,-1])



#       MATHEMATICAL FUNCTIONS
#These are functions that allow you to easily perform some mathematical operations. Some of these functions come with Python, while others are found in the math module.

#abs
#Returns the absolute value of a number.

x = abs(-71)
print(x)

#divmod
#Returns the quotient and the remainder of dividing two numbers.

x = divmod(5,2)
print(x) # (2,1)

#max
#Returns the largest number or string in the given values or iterable object.

x = max(5,2, 6,9) #9
print(x)

x = max("Mike", "John", "Vicky")
print(x)

#pow
#Returns the result of raising the first number to the power of the second number. If a third number is given, it computes the result modulo that number.

x = pow(5, 2) #25
x = pow(5, 2, 3) #1, the remainder when divided by 3.

#round
#Rounds a float number to the nearest integer, up or down, depending on the decimal part of the number. If the number of digits after the decimal point is given, the number is rounded to that many digits instead.

x = round(5.531)
x = round(5.431, 2) #show two digits after the decimal point instead of rounding.

#reversed
#Reverses the order of elements in an iterable object and returns it.

x = list(reversed([4,5,-3,-1]))
x = list(reversed(["p","y","t","h","o","n"]))

import math

#math.ceil
#Rounds a float number up to the next integer.

x = math.ceil(1.4)
print(x)

#math.floor
#Rounds a float number down to the previous integer.