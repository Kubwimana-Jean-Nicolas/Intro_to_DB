# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',       # replace with your host if different
        user='root',            # replace with your MySQL username
        password=''             # replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor.is_connected() is False:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
