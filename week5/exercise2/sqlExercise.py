#!C:/Users/Max/Anaconda/Python

import sqlite3
con = sqlite3.connect('../northwind.db')
cur = con.cursor()

# Join Orders and Order Details tables on OrderID column
# Filter by CustomerID 'ALFKI'
orderID_and_productID = cur.execute("""
					   SELECT Orders.OrderID, 'Order Details'.ProductID 
					   FROM 'Order Details' INNER JOIN Orders
					   ON Orders.OrderID='Order Details'.OrderID 
					   WHERE CustomerID='ALFKI'
					   """)

# Obtain human readable list of ID's
results = orderID_and_productID.fetchall()

# Print results
for order,product in results:
	print "Order number",order,"included the purchase of product number",product