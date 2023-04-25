

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are", drivers, "drivers only available"
print "There are", (cars - cars_driven), "free cars"
print "We can transport", car_pool_capacity, "people today"
print "We have", passengers, "for car pool today"
print "We need put", average_passengers_per_car, "on average per car today" 