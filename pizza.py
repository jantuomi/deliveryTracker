#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import openpyxl

# Let's call the excel file "data.xlsx"
filename = 'data.xlsx'
try:
    # Try opening the file
    wb = openpyxl.load_workbook(filename)

    # If it exists, get the active worksheet
    sheet = wb.active
except FileNotFoundError:
    # If the file didn't exist, create it
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Append some header data
    sheet.append(['Timestamp', 'Total price', 'Amount given', 'Tip', 'Trip distance', 'Net tip'])

# Rename the sheet
sheet.title = 'Delivery tracker'

# Save the file
wb.save(filename)

gas_cost = 0.08 #how much it costs to drive 1 mile
wear_tear = 0.1 #estimated 10 cents per mile in tire and engine wear
mpg = 30 # my car gets 30 miles per gallon
delivery_charge = 1.25 # dominos pays the driver $1.25 each delivery

while True:   
    now = datetime.datetime.now()
    print("|||WELCOME TO TIP TRACKER.  ALL OF THE DATA SHOWN IS BASED ON 30 MPG AT $2.60/GALLON AND 10¢ OF WEAR'N'TEAR EACH MILE|||")
    total_price = float(input('Total Price: ')) #Total price of order
    amt_given = float(input('Amount Given: ')) #Total amount of money received from customer
    tip = amt_given - total_price #This is your total Gross Tip
    print('Tip given = {}'.format(tip)) #This prints your tip and saves the tip as a variable ( I think..lol)
    trip_distance = float(input('Miles: ')) # This is your round trip distance in miles
    print ("Your net tip is...")

    net_tip = tip + delivery_charge -(gas_cost + wear_tear * trip_distance) #This prints your Net Tip after factoring in the delivery charge, gas, and wear n tear
    print (net_tip)

    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print ("Current date and time : ")
    print (timestamp)

    # Store the data in a new row in the file
    sheet.append([timestamp, total_price, amt_given, tip, trip_distance, net_tip])

    # Save the document
    wb.save(filename)
