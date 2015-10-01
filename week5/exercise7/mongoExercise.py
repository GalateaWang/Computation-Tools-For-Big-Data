#!C:/Users/Max/Anaconda/Python
import pymongo as pm

# Connection to database Northwind
client = pm.MongoClient()
db = client.Northwind

# Establish collections for orders, and orderDetails
order_collection = db.orders
orderDetails_collection = db['order-details']

# Find all orders made by user 'ALFKI'
orders = order_collection.find({'CustomerID':'ALFKI'})

# Generate list of ALFKI's orderID's for future comparison
orderIDs = []
for order in orders:
	if order['OrderID'] not in orderIDs:
		orderIDs.append(order['OrderID'])

productIDs = []
# Generate list of ProductID's from ALFKI's orderID's
for count in range(len(orderIDs)):
	
	# Select orders with corresponding orderID
	orders = orderDetails_collection.find({'OrderID':orderIDs[count]})
	
	# Copy down the order's ProductID
	for order in orders:
		if(order['ProductID'] not in productIDs):
			productIDs.append(order['ProductID'])
	
# Find all orderIDs for ALFKI's items
orderIDs = []
for productID in productIDs:
	# Select orders with corresponding orderID
	orders = orderDetails_collection.find({'ProductID':productID})
	
	# Copy down the order's ProductID
	for order in orders:
		if(order['OrderID'] not in orderIDs):
			orderIDs.append(order['OrderID'])

# Find all customerIDs that have ordered the same items
customerIDs = []
for orderID in orderIDs:
	# Select orders with corresponding orderID
	orders = order_collection.find({'OrderID':orderID})
	
	# Copy down the order's CustomerID
	for order in orders:
		if(order['CustomerID'] not in customerIDs):
			customerIDs.append(order['CustomerID'])
			
# Print results
print "The customers who have ordered the same products as customer ALFKI, including ALFKI himself, are:"
print customerIDs