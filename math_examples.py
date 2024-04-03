import math
import random
import statistics

root = math.sqrt(16)
print(root)

print(math.pi)
print(math.e)

print(round(5.4))
print(math.floor(5.4))
print(math.ceil(5.4))

print("--------------------")
rand_int = random.randint(1,10)
print(rand_int)

rand_range = random.randrange(1, 10)
print(rand_range)

random_float = random.random()
print(random_float)

rand_choice = random.choice([1, 2, 3, 4, 5])
print(rand_choice)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

print("========================")
date = [2, 4, 5, 6, 7, 89, 8, 43, 78]

date_mean = statistics.mean(date)
print(f"The mean of the date set is {date_mean}")

date_median = statistics.median(date)
print(f"The median of data set is {date_median}" )

