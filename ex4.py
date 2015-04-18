#Names and Variables

cars = 100
car_space=4.0
drivers=30
passengers=90
cars_undriven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*car_space
average=passengers/cars_driven

print('There are',cars,'cars available.')
print('There are only',drivers,'drivers available.\n')
print('There will be',cars_undriven,'empty cars today.')
print('We can transport',carpool_capacity,'people today.')
print('We need put',average,'in each car.')
