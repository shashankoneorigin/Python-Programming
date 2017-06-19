cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print("there are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "cars not driven today")
print("we can transport", car_pool_capacity, "people capacity today")
print("we have ", passengers, "to car pool today")
print("we need to put about ", average_passenger_per_car, "passengers per each car")
