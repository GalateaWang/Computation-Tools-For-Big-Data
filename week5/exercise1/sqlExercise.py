#!C:/Users/Max/Anaconda/Python
import sqlite3

conn = sqlite3.connect('../northwind.db')
c = conn.cursor()

# Generate list of original values and print
c.execute("SELECT CategoryID, Description FROM Categories")
rows = c.fetchall()
print rows

# Add new values 10, "hello_world"
c.execute("INSERT INTO Categories (CategoryID,Description) VALUES (10, 'hello_world')")

# Generate list of values and print
c.execute("SELECT CategoryID, Description FROM Categories")
rows = c.fetchall()
print rows

# Remove newly added values
c.execute("DELETE FROM Categories WHERE CategoryID=10")

# Generate list of values and print
c.execute("SELECT CategoryID, Description FROM Categories")
rows = c.fetchall()
print rows

