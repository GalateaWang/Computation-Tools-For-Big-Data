#!C:/Users/Max/Anaconda/Python
import sqlite3

conn = sqlite3.connect('../northwind.db')
c = conn.cursor()

c.execute("SELECT CategoryID, Description FROM Categories")

rows = c.fetchall()
print rows

c.execute("INSERT INTO Categories (CategoryID,Description) VALUES (10, 'hello_world')")

c.execute("SELECT CategoryID, Description FROM Categories")

rows = c.fetchall()
print rows

c.execute("DELETE FROM Categories WHERE CategoryID=10")

c.execute("SELECT CategoryID, Description FROM Categories")
rows = c.fetchall()
print rows

