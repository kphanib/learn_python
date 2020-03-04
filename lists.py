#What is the difference between `sorted(list)` vs `list.sort()`?
#sorted() returns a new sorted list, leaving the original list unaffected. list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).
my_list = [1,2,3,4,5]
my_new_list = []
for num in my_list:
    my_new_list.append(num-my_list[num-1])
print(my_new_list)
print(40*'-')
my_string = "level"
for letter in my_string[::-1]:
    print(letter, end=" ")
print()