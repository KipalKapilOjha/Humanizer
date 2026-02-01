import MySQLdb

try:
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS humanizer_db")
    print("Database created successfully")
except Exception as e:
    print(f"Error creating database: {e}")
