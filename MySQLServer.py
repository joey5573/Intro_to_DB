# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # الاتصال بالسيرفر (غيّر بيانات المستخدم وكلمة المرور حسب إعداداتك)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # غيّر هذا حسب إعدادات MySQL
            password="yourpassword"  # غيّر هذا حسب إعدادات MySQL
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
