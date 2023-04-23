#       Formatting Data in Python

#The format() function is used to format data in a specific way while printing in Python. It was introduced in Python 3, and before that, %s was used for formatting. However, it is still supported in Python 3.

# Single Parameter Formatting

print("Hello {}".format("John"))
name = "John"
print("Hello {}".format(name))


#Multiple Parameter Formatting

print("{}{}".format("one","two"))
print("{}{}".format(1,2))
print("{1}{0}".format("Ali","Veli"))
print("{name}{0}".format("apple" , name="Ahmet"))


#   Exercise
#Write a program using variables that prints the following message to the screen: "My name is Ahmet, and I'm 19 years old."

name = "Ahmet"
age = 19
print("My name is {}, and I'm {} years old.".format(name, age))


#   Formatting String Data

print("{:10}".format("test"))
print("{:>10}".format("test"))
print("{:_<10}".format("test"))
print("{:^10}".format("test"))


#   Truncation

print("{:.5}".format('xylophone'))
print("{:10.5}".format("xylophone"))


#   Formatting Integer Data

print("{:d}".format(42))
print("{}".format(42))
print("{: d}".format(42))
print("{:010d}".format(42))
print("{:>5}".format(42))


#   Formatting Float Data

print("{:.2f}".format(3.1281121))
print("{:.5f}".format(3.14))
print("{8.5f}".format(3.1411311))


#Using f-strings for Formatting
#In Python 3.6, a new string formatting approach was introduced using f-strings.

print(f"{2+5}")
name = "John"
lastname = "Doe"
print(f"Hello {name} {lastname}")
a = 5
b = 10
print(f"{a + b}, {2 + b}")


#   Exercise
#Calculate the area of a circle based on the given radius and display it with 2 digits after the comma using f-strings.

r = float(input("Enter the radius: "))
area = 3.14 * r**2
print(f"The area of the circle is {area:.2f}")


#   Exercise
#Calculate the volume of a cylinder based on the given radius and height, and display it with 3 digits after the comma using the format() function.

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
V = 3.14 * r**2 * h
print("The volume of the cylinder is {:.3f}".format(V))


#   Exercise
#Calculate the current based on the given resistance and voltage values entered by the user and display it with 3 digits after the comma using f-strings.

resistance = int(input("Enter resistance: "))
voltage = int(input("Enter voltage: "))
current = voltage / resistance
print(f"The current is {current:.3f}")