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
					   """)

# Obtain human readable list of ID's
results = orderID_and_productID.fetchall()

# Obtain list of order numbers made by each customer above
orders = []
for customer in results:
	orderIDs = cur.execute("""
						SELECT Orders.OrderID
						FROM Orders
						WHERE CustomerID=(?)""",(customer)
						).fetchall()
	for orderID in orderIDs:
		if orderID not in orders:
			orders.append(orderID)

# Obtain list of unique products corresponding to orderIDs found above
products = []
for order in orders:
	productIDs = cur.execute("""
						SELECT 'Order Details'.ProductID
						FROM 'Order Details'
						WHERE OrderID=(?)""",(order)
						).fetchall()
	for productID in productIDs:
		if productID[0] not in products:
			products.append(productID[0])
			
# Print results
print "The number of different products purchased by pear-purchasing customers is: ", len(products)
print "The productIDs of those products are shown here:"
print products
