cost = 100
age = 70
time = (11, 30)

if age <= 12:
    print(cost * 0.5)
elif age >= 60:
    print(cost * 0.7)
elif (time[0] * 60 + time[1]) < 17 * 60:
    print(cost * 0.8)
else:
    print(cost)



