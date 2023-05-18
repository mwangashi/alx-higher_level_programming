import mysql.connector

# Set up the connection parameters
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'information_schema'  # We'll query the 'information_schema' database
}

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(**config)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute the query to retrieve database names
    cursor.execute("SELECT SCHEMA_NAME FROM SCHEMATA")

    # Fetch all the results
    databases = cursor.fetchall()

    # Print the database names
    for db in databases:
        print(db[0])

except mysql.connector.Error as error:
    print("Error while connecting to MySQL:", error)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()

