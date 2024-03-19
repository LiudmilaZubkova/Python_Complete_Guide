empty_dict = {}
print(empty_dict)

my_dict = {"first_name": "Liudmila", "last_name": "Zubkova", "age": 41}
print(my_dict)
print(f"{my_dict['first_name']} is {my_dict['age']} years old")

my_dict["lenguage"] = "Python"
print(my_dict)

my_dict["lenguage"] = "Java"
print(my_dict)

del my_dict["lenguage"]
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) # list of tuples