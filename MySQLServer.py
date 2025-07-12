import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (change user/password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root"  # Replace with your MySQL password
        )

        cursor = connection.cursor()

        # Create database (does not use SELECT or SHOW)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
