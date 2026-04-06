import mysql.connector

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        auth_plugin="mysql_native_password"  # add this
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS news_db")
    conn.commit()
    cursor.close()
    conn.close()

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="database",
        auth_plugin="mysql_native_password"  # add this
    )
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS headlines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        headline TEXT,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
