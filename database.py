import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MR2003@mohini",
    database="job_tracker"
)

if conn.is_connected():
    print("Database Connected Successfully")