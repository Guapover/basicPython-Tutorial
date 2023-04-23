#COMMENT LINES

#       Single line comments
a = 5 # assign 5 to variable a

#       Multi-line comments
"""
Some
multi-line
comments
"""

'''
Some
multi-line
comments
'''

#       OUTPUT OPERATION

#In Python, you can use the print() function to output a value to the console.

print("mustafa") #mustafa

print(1231) #1231

print(36.2) #36.2

print(True) #True

print(not True) #False

print("Mustafa"+"Turhan") #MustafaTurhan

print(2+1 ,"mustafa" + " Turhan") #3 mustafa Turhan

print("istanbul", end= "-") #istanbul-

print() #adds a new empty line

#       INPUT OPERATION
#You can use the input() function to get input from the user.
#The input() function always returns the data as a string.

name = input("Please enter your name: ")
print("Welcome " , name)

age = input("Please enter your age: ")
print(age + 2 )

#       TYPE CONVERSIONS

#The int() function converts data to an integer.

age =int( input("Please enter your age: "))

print(age + 2 )

height = int(input("Please enter your height: " ))
print(height)

#The float() function converts data to a floating-point number.

height = float(input("Please enter your height: " ))
print(height + 100)

age = input("Please enter your age")
print( "Your sibling's age is", int(age) - 3)

