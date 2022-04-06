#!/bin/python3


# Variables
quote = "Everything is fair in love and war."
print(quote)

#Mehods
print(quote.upper())
print(quote.lower())
print(quote.title())

# Get Length
print(len(quote))

name = "Anik Hossain"
age = 25

print("My name is " + name + " and I am " + str(age) + " years old.")
print("\n")

# Functions
print("Here is  an example of Function")

def who_am_i(): #Define a Function
	name = "Anik Hossain"
	age = 25
	email = "anik.wdev@gmail.com"
	print("Hello, my name is " + name + " and  I am " + str(age) + " years old.")
	
# Call the Function
who_am_i()

def who_are_you(name, age): #Define another Function
	print("Hello, my name is " + name + " and  I am " + str(age) + " years old.")
	
# Call another Function
who_are_you("Mr. X", 50)


# Multiply your numbers
def multiply(x, y):
	return x * y
	
#Call the function and print the result
print(multiply(45, 6))

def squire_root(x):
	print(x ** .5)
	
#
squire_root(64)

# New Line Function
def nl():
	print("\n")
	
nl()

#Skip 2 Lessons

#Conditional Statements
def chocolate(money):
	if money >= 2:
		return "You can buy a chocolate"
	else:
		return "Sorry you have no enough money"
		

print(chocolate(10))



















