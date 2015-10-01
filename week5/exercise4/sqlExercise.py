#!C:/Users/Max/Anaconda/Python

import sqlite3
con = sqlite3.connect('../northwind.db')
cur = con.cursor()

# Join Orders and Order Details tables on OrderID column
# Filter by CustomerID 'ALFKI'
orderID_and_productID = cur.execute("""
					   SELECT Orders.CustomerID,'Order Details'.Quantity
					   FROM 'Order Details' INNER JOIN Orders
					   ON Orders.OrderID='Order Details'.OrderID 
					   WHERE ProductID='7'
					   """)

# Obtain human readable list of ID's
results = orderID_and_productID.fetchall()

orderDict = dict()
for customer, qty in results:
	if customer in orderDict.keys():
		orderDict[customer] += qty
	else:
		orderDict[customer] = qty
		
for customer in orderDict.keys():
	print "Customer",customer,"ordered",orderDict[customer],"of 'Uncle Bob's Organic Dried Pears'"
