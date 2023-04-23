#       Control Structures
#1. IF statement
a = 6
if a == 6: # CONDITION
    print("The value of a is ", a)

#EXAMPLE:
#Let's ask the user for a password. If this password matches the password we previously set, print the message "Correct Password".
old_password = "12345"
password = input("Password: ")

if old_password == password:
    print("Correct Password")

number = 45
if 30 < number < 50:
    print("The number is between 30 and 50")
    print("Program finished")

#EXAMPLE:
#If the entered positive integer is divisible by both 5 and 7, print "Lucky Number" to the screen.
number = int(input("Enter a number: "))

if number % 5 == 0 and number % 7 == 0:
    print("Lucky Number")

#What if the condition we wrote is not satisfied? We need to think of something for this case.
#For this, we can use else.
grade = 45
if grade > 50:
    print("Passed")
else:
    print("Failed")
    print("Program finished")

#EXAMPLE :
#If the condition inside if is not satisfied, the program will continue with the else statement and execute the else block.
answer = input("Is it raining? ")
if answer == "yes":
    print("Take an umbrella")
else:
    print("Wear a hat")

#Writing if statement in one line
#We can write an expression with if and else statements in one line. We should write the positive (true) situation to the left of if and the negative (false) situation to the right of else.
a = 6
answer = "ok" if a == 6 else "no"
print(answer)

#Writing if..elif..else
#If you have more than two options to decide, you can use the if..elif..else structure. You can use as many elif statements as your conditions.
num = 10
if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
else:
    print("Number is greater than zero")

#Nested if statements
#There may be situations where you need to make different decisions inside a decision block.
age = 20
if age >= 18:
    print("Adult")

else:
    if age >= 13:
        print("Teenager")
    else:
        print("Child")

#Check a specific username and password information in sequence with the entered username and password information.
username = input("Username: ")

if username == "Mustafa":
    password = int(input("Password: "))
    if password == 12345:
        print("Successful login")
    else:
        print("Your password does not match")
else:
    print("There is no such username")

#Show the profit-loss situation according to the purchase and sale price.
purchase_price = float(input("Purchase price: "))
sale_price = float(input("Sale price: "))

if purchase_price > sale_price:
    print("Loss: ", purchase_price - sale_price)

elif purchase_price == sale_price:
    print("There is no profit or loss")
else:
    print("Profit: ", sale_price - purchase_price)