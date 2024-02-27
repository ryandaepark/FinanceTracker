#Adding test data through Python

# Importing necessary libraries
import sqlite3
from datetime import datetime, timedelta
import random

# Define the path to your SQLite database
db_path = './data/finance_tracker.db'

# Connect to the SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Commit the changes
conn.commit()

# Function to generate test data
def generate_test_data(num_entries=20):
    for _ in range(num_entries):
        category_id = random.randint(0, 6)  # Assuming there are 5 categories
        amount = round(random.uniform(-1000, 1000), 2)  # Generate amounts between -1000 and 1000
        description = f"Test transaction {_}"
        transaction_date = (datetime.now() - timedelta(days=random.randint(1, 365))).date()  # Random date within the last year
        
        # Insert generated data into the transactions table
        cursor.execute('''
        INSERT INTO transactions (category_id, amount, description, transaction_date)
        VALUES (?, ?, ?, ?)
        ''', (category_id, amount, description, transaction_date))

# Generate and insert the test data
generate_test_data()

# Commit the insertions and close the connection
conn.commit()
conn.close()

print("Test data generated and inserted successfully.")