import mariadb
import sys

try:
    # Connect to MariaDB
    conn = mariadb.connect(
        user="your_username",
        password="your_password",
        host="your_host",
        port=your_port,
        database="your_database"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM your_table")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)
