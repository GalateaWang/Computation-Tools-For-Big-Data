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

# Generate list of orderID's for future comparison
orderIDs = []
for order in orders:
	if order['OrderID'] not in orderIDs:
		orderIDs.append(order['OrderID'])

allProducts = []
# Generate list of ProductID's from orderID's
for count in range(len(orderIDs)):
	productIDs = []
	
	# Select orders with corresponding orderID
	orders = orderDetails_collection.find({'OrderID':orderIDs[count]})
	
	# Copy down the order's ProductID
	for order in orders:
		if(order['ProductID'] not in productIDs):
			productIDs.append(order['ProductID'])
		
	allProducts.append(productIDs)

# Print off results
for count in range(len(orderIDs)):
	for product in range(len(allProducts[count])):
		print "Order ID",orderIDs[count], "was for product number",allProducts[count][product]