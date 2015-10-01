#!C:/Users/Max/Anaconda/Python

import sqlite3
con = sqlite3.connect('../northwind.db')
cur = con.cursor()

# Join Orders and Order Details tables on OrderID column
# Filter by ProductID '7'
orderID_and_productID = cur.execute("""
					   SELECT Orders.CustomerID
					   FROM 'Order Details' INNER JOIN Orders
					   ON Orders.OrderID='Order Details'.OrderID 
					   WHERE ProductID='7'
					   """).fetchall()

# Obtain list of order numbers made by each customer above
orders = []
for customer in orderID_and_productID:
	orderIDs = cur.execute("""
						SELECT Orders.OrderID
						FROM Orders
						WHERE CustomerID=(?)""",(customer)
						).fetchall()
	for orderID in orderIDs:
		if orderID not in orders:
			orders.append(orderID)

# Obtain count of orders for each unique products corresponding to orderIDs found above
productCount = dict()
for order in orders:
	productIDs = cur.execute("""
						SELECT 'Order Details'.ProductID
						FROM 'Order Details'
						WHERE OrderID=(?)""",(order)
						).fetchall()
	for productID in productIDs:
		if productID != (7,):
			if productID not in productCount.keys():
				productCount[productID] = 1
			else:
				productCount[productID] += 1

# Print results
maxOrders = max(productCount.values())
for product in productCount:
	if productCount[product] == maxOrders:
		print "Product",product[0],"has been ordered the most, a total of",productCount[product],"times."
