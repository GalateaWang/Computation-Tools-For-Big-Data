#!C:/Users/Max/Anaconda/Python
import pymongo as pm

# Connection to database Northwind
client = pm.MongoClient()
db = client.Northwind

# Establish collections for orders, and orderDetails
order_collection = db.orders
orderDetails_collection = db['order-details']

# Find all orders made by for productID 7
orderDetails = orderDetails_collection.find({'ProductID':7})

# Generate list of unique orderID's for future comparison
# and the quantity associated with each order
allOrderIDs = []
for order in orderDetails:
	if order['OrderID'] not in allOrderIDs:
		allOrderIDs.append(order['OrderID'])

# Generate list of users associted with each orderID
users = []
for count in range(len(allOrderIDs)):
	orders = order_collection.find({'OrderID':allOrderIDs[count]})
	for order in orders:
		users.append(order['CustomerID'])
		break

# Generate list of orderID's from each customer who
# bought peaches
orderIDs = []
for user in users:
	orders = order_collection.find({'CustomerID':user})
	for order in orders:
		orderIDs.append(order['OrderID'])

# Geneerate a list of products from orderIDs of
# customers who bought peaches
productIDs = []
for order in orderIDs:
	products = orderDetails_collection.find({'OrderID':order})
	for product in products:
		if product['ProductID'] not in productIDs:
			productIDs.append(product['ProductID'])

# Print results
print "The number of different products purchased by pear-purchasing customers is:",len(productIDs)
print "The productIDs of those products are shown here:"
print productIDs