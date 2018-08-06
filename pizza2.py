import datetime
while True:
   
    gas_price = 2.6 #Avg gas price in NC
    wear_tear = 0.1 #estimated 10 cents per mile in tire and engine wear
    mpg = 30 # my car gets 30 miles per gallon
    delivery_charge = 1.25 #dominos pays the driver $1.25 each delivery
    now = datetime.datetime.now()
    print("Tip Tracker.  All data based on 30 mpg at $2.60 a gallon and 10 cents of wear n tear each mile")
    total_price = float(input('Total Price: ')) #Total price of order
    amt_given = float(input('Amount Given: ')) #Total amount of money received from customer
    tip = amt_given - total_price #This is your total Gross Tip
    print('Tip given = {}'.format(tip)) #This prints your tip and saves the tip as a variable ( I think..lol)
    trip_distance = float(input('Miles: ')) # This is your round trip distance in miles
    print ("Your net tip is...")
    print (tip + delivery_charge -(gas_price / trip_distance + tip * wear_tear)) #This prints your Net Tip after factoring in the delivery charge, gas, and wear n tear
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
