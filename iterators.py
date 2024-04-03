fruits = ['apple', 'banana', 'cherry']
fruits_iter = iter(fruits)

print(next(fruits_iter))
print(next(fruits_iter))
print(next(fruits_iter))

def squares(n):
    for i in range(1, n+1):
        yield i * i

squers_gen = squares(5)

for num in squers_gen:
    print(num)