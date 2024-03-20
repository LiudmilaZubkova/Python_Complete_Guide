n = 10
total_sum = 0
for i in range(n):
    if (i % 3 == 0) or (i % 5 == 0):
        total_sum +=i
print(total_sum)

n_1 = 5
total_sum_1 = 0
j = 1
while j < n_1:
    if (j % 3 == 0) or (j % 5 == 0):
        total_sum_1 += j
    j += 1
print(total_sum_1)
