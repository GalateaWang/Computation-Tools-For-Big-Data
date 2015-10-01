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
qty = []
for order in orderDetails:
	if order['OrderID'] not in allOrderIDs:
		allOrderIDs.append(order['OrderID'])
		qty.append(order['Quantity'])

# Generate list of users associted with each orderID
users = []
for count in range(len(allOrderIDs)):
	orders = order_collection.find({'OrderID':allOrderIDs[count]})
	for order in orders:
		users.append(order['CustomerID'])
		break

# Create dictionary relating each customer with qty
# of item purchased
orderDict = dict()
for i in range(len(users)):
	if users[i] in orderDict:
		orderDict[users[i]] += qty[i]
	else:
		orderDict[users[i]] = qty[i]

# Print results
for user in orderDict:
	print "Customer",user,"ordered",orderDict[user],"of 'Uncle Bob's Organic Dried Pears'"