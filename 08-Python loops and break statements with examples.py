#       Loops
#Loops are control statements that allow a group of statements to be executed repeatedly.
#Programs spend most of their runtime executing loops.
#There are two types of loops in Python: for loops and while loops.


#Example -1
for i in [1, 2, 3, 4, 5]:
    print(i)

#Example -2
a = [1,2,3,4,5]
for i in a:
    print(i, end =" ")

#Example -3
total = 0
for i in [1,2,3,4,5]:
    total = total + i
    print(total)

#       The Range Function
#How can we use Python for loops to iterate over incremental or decremental values,
#such as a for loop that goes from 1 to 10? In Python, we use the range() function for this.
#The range function returns a traversable object consisting of integers within a specific range.
#range(1, 10) = 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1,51):
    print(i, end=" ")

#xample -4
import time
for i in range(10):
    time.sleep(0.5)
    print(i)

#Example -5
for i in range(10,20):
    print(i)

#Example -6
for i in range(1,10,2):
    print(i)

#Example -7
for i in range(10,0,-2):
    print(i)

#Example -8
for i in range(10):
    print("Hello")

#Example -9
for i in range(10):
    print("Hello")
print("There")

#Example -10
for i in range(10):
    print("Hello")
print("There")

#Example -11
a = 0
for i in range(10):
    a = a + 1
print(a)

#Question -01
#Print the squares of numbers from 1 to 50. For example,
"""
The square of 1 = 1
The square of 4 = 16
"""

for i in range(1,51):
    print(f"The square of {i} = {i**2}")

#Print the 8 times table using a for loop.
"""
1 x 8 = 8
2 x 8 = 16
3 x 8 = 24
...
10 x 8 = 80
"""

for i in range(1,11):
    print(f"{i} x 8 = {i * 8}")

#Write a program that prints the following output:
"""

"""

for i in range(4):
    for j in range(5):
        print("*", end="")
print()

#Write a program that prints the following output:
"""
12345
12345
12345
12345
"""

for i in range(4):
    for j in range(1,6):
        print(j,end="")
print()

for j in range(1,6):
    for i in range(5):
        print(j,end="")
print()

for j in range(5,0,-1):
    for i in range(j):
        print("*", end="")
print()

#   Break
#How can we exit a loop in the middle of its execution?
#The break statement can be used within loops to exit the loop and execute the statements following the loop.
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:
        break
    print(i)
print("Exited the for loop")

nums = [1, 2, 3, 4, 5, 6]
n = 4
for num in nums:
    if n == num:
        break
    else:
        print(num)
print(f"Number found: {n}")

for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 0:
        continue
    print(i)
print("Done")