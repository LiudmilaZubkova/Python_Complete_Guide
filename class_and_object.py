from car import Car

my_car = Car("Toyota", "Camry", "2014")
friend_car = Car("Toyota", "Rav4", 2020)

my_car.drive(100)
friend_car.drive(50)

Car.set_wheels(8)
print(my_car.wheels)
print(friend_car.wheels)

kilometers = Car.miles_to_kilometers(100)
print(kilometers)

kilometers_2 = my_car.miles_to_kilometers(100)
print(kilometers_2)