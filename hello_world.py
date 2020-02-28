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


#Compound data types: Lists, Dict, Tuples, Sets
#lists
my_list = [1,2,"name","place"]
print(my_list[0])
my_list = [1,2,3,4,5,6,7,8]
print(my_list[::-1])
print(type(my_list))
#dictionary 
my_dict = {1:2, "name":"python"}
print(my_dict["name"])
print(type(my_dict))
my_dict = {'name':'john','course':'python'}
#print(my_dict[::-1])
#sets
# my_set_1 = {1,2,"name","name"}
# print(my_set_1) #gets rid of all duplicates
# print(type(my_set_1))
my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python',6}
my_second_set = {6,2,'javascript','rails',8,9,10,21,1000,'c'}
my_set.update(my_second_set)
print(my_set)
#tuples
#tuples are immutable and don't support item reassignment 
my_tuple = (1,2,"name","age")
print(my_tuple)
print(type(my_tuple))