# ✅ Strings are always assigned with a Variable
# ' in middle of String Ex: "Anu's World"
# For multi line String use """ ..... """
# we use len() for length of a Character in a String
# we use index[] in string to print particular word[0] [0:5]
# Ex: msg = Hello World here we print(msg[0]) o/p is H
# and for print(msg[0:5]) o/p is Hello, index = total length - 1
# Methods like .lower(), .upper(), count(), find(), .replace()
# String concatenation with + operator
# f-strings are better to use variables inside a string f''
# index = len(word) - 1


# ✅ In List, we have methods like variable.append(), .insert(includes index),
# .extend(), .remove(), .pop(), .sort(), var_1 = sorted(variable), .index()
# min(), max(), sum()
# To check a value is in our list  or not we can use 'in'
# Ex: univ = ['sun', 'moon', 'star', 'cosmic'] print('earth' in univ)
# it gives False o/p
# we can also loop through items in our list using for loops
# we use enumerate() to get index and value of list
# Ex: univ = ['sun', 'moon', 'star'] we can use .join(), .split()
# for index, item in enumerate(univ, start=1):
#     print(index, item) o/p is
# 1 sun  here it started with 1 bcz we put start=1
# 2 moon
# 3 star
# for mutable objects we can change the values in list
# for immutable objects we cannot change the values in list

# ✅ Tuples, are immutable bcz they cannot change once created
# you can loop through tuples if you don't want to change values

# ✅ Sets, are values that are unordered & they have no duplicates
# Every time you run the Sets, they change their order of items in Sets
# cs_courses = {'Java', 'C', 'C++', 'C'}
# print('C' in cs_courses)
# we can ask if an item is in Set or not
# and it returns a Bool value True or False as o/p
# In Sets, Methods like .intersection(), .difference(), .union()
# for comparing and checking existing items in both Sets
# To create Empty Lists, Tuples, Sets

# empty_list = [] we can use anyone in these both lists
# empty_list = list()
# empty_tuple = () we can use anyone in these both tuples
# empty_tuple = tuple()
# empty_set = set() this is the only way for Sets

# ✅ Dictionaries
# student = {'name': 'John', 'age': 24, 'courses': ['C', 'C++','Java']}
# print(student['name']) o/p is John to get specific value key
# print(student) gets everything in dictionary
# student = {'name': 'John', 'age': 24, 'courses': ['C', 'C++','Java']}
# student['phone'] = 7837909809 o/p prints all key value pairs including phone
# print(student.get('phone', 'Not Found')) o/p is 7837909809
# we can also have .update() method to update key value pairs
# orelse you can simply update manually
# del method to delete a key value pair Ex: save = {'a':'b', 'ef':'gh'}
# del save['ef']
# print(save) o/p is {'a':'b'}
# with del method you cannot use or return the deleted value again
# also you can use .pop() method to remove a key value pair but can be returned again
# we can also use len() to check how many key value pairs are present
# we have .keys(), .values(), .items() to check how many key n values are present
# we use for loops to loop through key n values

# input() — INSIDE or OUTSIDE LOOP?
# ✅ input() OUTSIDE loop
# Use when value is fixed
#
# n = int(input("Enter number: "))
# for i in range(n):
#     print("Hello")
#
# ✅ input() INSIDE loop
# Use when value keeps changing
#
# while True:
#     word = input("Enter word: ")
#     if word == "stop":
#         break

# ✅ Rule 1

# If the value is needed only once and reused
# ➡ input() goes outside the loop

# ✅ Rule 2

# If the value must be taken again and again
# ➡ input() goes inside the loop
#
# This rule applies to both for and while


# 🔑 RULE 1: USE A COUNT VARIABLE WHEN YOU ARE COUNTING SOMETHING

# Examples:
#
# How many vowels in a word
#
# How many times user entered a wrong password
#
# How many even numbers
#
# How many loops ran
#
# How many characters satisfy a condition

