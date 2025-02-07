import mysql.connector
def get_mysql_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sales_mart"
    )
    return connection