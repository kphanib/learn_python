print("hello world")
#slicing
a = "interstellar"
print(a[0:5]) #inter
print(a[5:]) #stellar
#stepsize 
print(a[2:5:2])
#methods and functions that can be used on string objects
"""len() type() id() capitalize() upper() lower() strip() find() split() join()"""
print(len(a))
print(type(a))
print(a.capitalize())
print(a.lower())
print(a.upper())
print(id(a))
#object a is assigned within a function example: len(a)
#object a is assigned to a method example: a.upper()
word_to_test = "level"
print(word_to_test[::-1])
my_daily_thought = "I am the first half I am the second half"
print(len(my_daily_thought)//2)
print(my_daily_thought[20:])
my_string = "There's a lot going on in the universe don't you think?"
print(len(my_string[::2]))

#clean format usage | string interpolation
print("hello {}".format("world"))

"""special characters
\ escape character which escapes a special character
\n new line character 
\t adds tabs within string"""

name_of_book = "Harry Potter"
name_of_book.upper()
name_of_book = name_of_book[::-1]
new_name_of_book = name_of_book
new_name_of_book.lower()
name_of_book = new_name_of_book.upper()
new_name_of_book = name_of_book[::-1]
print(name_of_book)
print(new_name_of_book)

# Numbers, integers, floats
print(int(100/3.3))
l = [9,4,8,200,62,35,12]
mid = len(l)//2
print(mid)
print(l[3])

#control the execution flow of a program by boolean and conditional tests along with branching 
#exercise 2


#Compund data types: Lists, Dict, Tuples, Sets
