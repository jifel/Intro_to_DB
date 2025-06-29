#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="0WholeNewLife@5"    
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
