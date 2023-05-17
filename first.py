#!/bin/python3

print("Hello, world!")

#STRINGS
#print string
print("hello world")
print('hello world')
print(""" This string runs
multiple lines """) #tripple quote for multi-line comment
print("This string is "+"awesome") #we can also concatenate
print('\n') #new line
print('Test that new line out!')

print('\n')
#MATH
print(50 + 50) #add
print(50 - 50) #substract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes whats left over
print(50 / 6) #division with remainder (or float)
print(50 // 6) #no remainder

print('\n')
#VARIABLES AND METHODS
quote = "All is fair in love and war"
print(quote)

#METHODS
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case - capitalize every first letter
print(len(quote)) #counts characters including spaces

name = "Thadeus" #string
age = 33 #int
gpa = 3.7 #float

print(age) #prints 33
print(int(30.1)) #prints 30 - will it round? No
print("My name is "+name+" and i am "+str(age)+" years old.")

age += 1 #variables can change
print(age) #34

birthday = 1
age += birthday
print(age) #35