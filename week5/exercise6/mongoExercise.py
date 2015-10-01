#!C:/Users/Max/Anaconda/Python
import pymongo as pm
import operator

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
		if order['OrderID'] not in orderIDs:
			orderIDs.append(order['OrderID'])

# Geneerate a dictionary of products from orderIDs of
# customers who bought peaches, counting how many times
# each product was ordered
productCount = dict()
for order in orderIDs:
	products = orderDetails_collection.find({'OrderID':order})
	for product in products:
		curr_product = product['ProductID']
		if curr_product != 7:
			
			#WTF why is it x3
			#USE GREG'S CODE
			if curr_product not in productCount.keys():
				productCount[curr_product] = 1.0/3
			else:
				productCount[curr_product] += 1.0/3
# Print results
maxOrders = max(productCount.values())
for product in productCount:
	if productCount[product] == maxOrders:
		print "Product",product,"has been ordered the most, a total of",productCount[product],"times."
