# any number of arguments
def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)

sum_numbers(2, 3, 4)
sum_numbers(1, 1, 8, 2, 0)

def display_fruits(fruits_list):
    for fruit in fruits_list:
        print(fruit)

my_fruits = ["apple", "peach", "cherry"]
display_fruits(my_fruits)

def multiplay(a, b):
    result = a * b
    return result

result = multiplay(5, 7)
print(result)
# In this case tuple will be returned
def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

result_sum, result_diff = calculate(10, 8)
print(f"Sum: {result_sum}, Diff: {result_diff}")

def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


average = calculate_average([1 ,3 , 4])
print(f"Average is {average:.2f}")