import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables

load_dotenv()

# Step 1: Connect to database via mysql.connector tool


def stream_users():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("host"),
            database='ALX_prodev',
            user=os.getenv("user"),
            password=os.getenv("password"),
            port=3306
        )
    except Error as e:
        print(f"Error connecting to Database...{e}")

    # Step 2: Create cursor object
    cursor = mydb.cursor(dictionary=True)

    # Step 3: Execute query using yield keyword
    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    finally:
        # Step 4: Close cursor and db connection
        cursor.close()
        mydb.close()


# for user in stream_users():
#     print(user)
