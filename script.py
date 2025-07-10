import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Step 1: Connect to server (import values from env variables (dotenv))

mydb = mysql.connector.connect(
    host=os.getenv("host"),
    port=3306,
    user=os.getenv("user"),
    database=os.getenv("database"),
    password=os.getenv("password"))

# check connection
if mydb.is_connected():
    print("Connection successful....")
    print("MySQL Server version:", mydb.server_info)

# Step 2: Get a cursor
mycursor = mydb.cursor()

# Step 3: Execute a query
# Create a table named `customers` (if it doesn't exist)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
)
""")

print("Table created successfully!")

# Insert some customer data
sql = "INSERT INTO customers (firstName, lastName, email) VALUES (%s, %s, %s)"
val = ("Mercy", "Johns", "mercy.johns@example.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

# Step 4: Fetch Results
# Read all customer data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

print("Customers:")
for row in myresult:
    print(row)


# Step 5: Close connection
mycursor.close()
mydb.close()
