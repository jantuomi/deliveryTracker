gas_price = 2.6
wear_tear = 0.1
mpg = 30
total_price = float(input('Total Price: '))
amt_given = float(input('Amount Given: '))
tip = amt_given - total_price
print('Tip given = {}'.format(tip))
trip_distance = float(input('Miles: '))
print (tip-(gas_price / trip_distance + tip * wear_tear))

