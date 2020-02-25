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