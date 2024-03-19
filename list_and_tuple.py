empty_list = []
print(empty_list)

my_list = [1, 2, 3,"a", 3.14]
print(my_list)
print(my_list[0])

sliced_list = my_list[1:4] # The last index does not include
print(sliced_list)

print(len(my_list))
my_list.append(10)
print(my_list)
my_list.extend([13, 'peach'])
print(my_list)
my_list.insert(0, 'zero') # insert before position
print(my_list)
print(my_list.count(3))
my_list.append(10)
print(my_list)
print(my_list.index(10)) # find first, doesn't find all

# We can not append, extend, insert and change items
# Tuples are faster. They require less memory space.
empty_tuple = ()
my_tuple = (1, 2, 3,"a", 3.14)
print(my_tuple[1:4])