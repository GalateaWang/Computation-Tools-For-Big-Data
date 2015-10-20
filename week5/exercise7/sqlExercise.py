#!C:/Users/Max/Anaconda/Python

import sqlite3
con = sqlite3.connect('../northwind.db')
cur = con.cursor()

# Join Orders and Order Details tables on OrderID column
# Filter by CustomerID 'ALFKI'
productID = cur.execute("""
					   SELECT 'Order Details'.ProductID
					   FROM 'Order Details' INNER JOIN Orders
					   ON Orders.OrderID='Order Details'.OrderID 
					   WHERE CustomerID='ALFKI'
					   """)

# Obtain human readable list of ID's
ALFKI_products = productID.fetchall()

# Find OrderIDs of all orders for relevant products
orderIDs = []
for product in ALFKI_products:
	orders = cur.execute("""
						SELECT 'Order Details'.OrderID
						FROM 'Order Details'
						WHERE ProductID=(?)""",(product)
						).fetchall()
	for order in orders:
		if order not in orderIDs:
			orderIDs.append(order)

# Find customers who made those orders
customerIDs = []
for order in orderIDs:
	customers = cur.execute("""
						 SELECT Orders.CustomerID
						 FROM Orders
						 WHERE OrderID=(?)""",(order)
						 ).fetchall()
	for customer in customers:
		if customer not in customerIDs:
			customerIDs.append(customer)
print "The customers who have ordered the same products as customer ALFKI, including ALFKI himself, are:"
print customerIDs
