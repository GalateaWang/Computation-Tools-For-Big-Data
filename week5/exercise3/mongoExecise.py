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
allorderIDs = []
for order in orders:
	if order['OrderID'] not in allorderIDs:
		allorderIDs.append(order['OrderID'])

# Initialize new lists. allProducts is a list of lists, containing
# the products for each order. repeatedorderIDs is a list of the orders
# containing MULTIPLE products
allProducts = []
repeatedorderIDs = []
# Generate list of ProductID's from orderID's
for count in range(len(allorderIDs)):
	productIDs = []
	
	# Select orders with corresponding orderID
	orders = orderDetails_collection.find({'OrderID':allorderIDs[count]})
	
	# Copy down the order's ProductID
	for order in orders:
		if(order['ProductID'] not in productIDs):
			productIDs.append(order['ProductID'])
	
	# If multiple orders, add to both lists
	if len(productIDs) > 1:
		allProducts.append(productIDs)
		repeatedorderIDs.append(allorderIDs[count])

# Print off results
for count in range(len(allProducts)):
	for product in range(len(allProducts[count])):
		print "Order ID",repeatedorderIDs[count], "was for product number",allProducts[count][product]