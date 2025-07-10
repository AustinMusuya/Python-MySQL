import os
import mysql.connector
import csv
import uuid
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Step 1: Connect to the mysql database server


def connect_db():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("host"),
            port=3306,
            user=os.getenv("user"),
            password=os.getenv("password")
        )
        return mydb
    except Error as e:
        print(f"Connection error: {e}")
        return None


# connection = connect_db()


# Step 2: Create the database ALX_prodev if it does not exist

def create_database(connection):
    try:
        cursor = connection.cursor()
        # excute query to create database ALX_prodev

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ALX_prodev"
        )
        print("Database ALX_prodev created Successfully.")
    except Error as e:
        print('Connection Error: {e}')
    finally:
        # close connection
        cursor.close()

# Step 2: Connect the the ALX_prodev database in MYSQL


def connect_to_prodev():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("host"),
            port=3306,
            user=os.getenv("user"),
            database="ALX_prodev",
            password=os.getenv("password")
        )
        return mydb
    except Error as e:
        print(f"Connection error: {e}")
        return None

# Step 2: Create a table user_data if it does not exists with the required fields


def create_table(connection):
    try:
        cursor = connection.cursor()
        # execute query to create table ALX_prodev

        # Create a table named `user_data` (if it doesn't exist)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        age DECIMAL NOT NULL
        )
        """)
        print("Table  user_data created Successfully.")
    except Error as e:
        print(f'Connection Error: {e}')
    finally:
        # close connection
        cursor.close()

# Step 2: Inserts data in the database if it does not exist


def insert_data(connection, data):
    cursor = connection.cursor()
    sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
    try:
        with open(data, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                user_id = str(uuid.uuid4())
                val = (user_id, row['name'], row['email'], row['age'])
                cursor.execute(sql, val)

        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
