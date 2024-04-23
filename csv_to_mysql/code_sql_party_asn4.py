import csv
import mysql.connector
from datetime import datetime


def convert_to_mysql_date(date_string):
    # Define a dictionary to map abbreviated month names to their numeric values
    month_dict = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
        'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
        'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    # Split the date string into day, month, and year
    day, month_str, year = date_string.split('/')
    
    # Convert month abbreviation to numeric value
    month = month_dict.get(month_str.lower())
    if not month:
        raise ValueError("Invalid month abbreviation")

    # Convert to MySQL date format
    mysql_date = datetime(int(year), month, int(day)).strftime('%Y-%m-%d')
    return mysql_date


table_name = 'party'
csv_file_path = 'output_party.csv'

# MySQL connection parameters
connection = mysql.connector.connect(
    host='localhost',
    database='assgnment4',
    user='root',
    password='mayurt'
)
cursor = connection.cursor()

# Create table in MySQL (if not exists)
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    `Sr_No` INT PRIMARY KEY,
    `Date_of_Encashment` DATE,
    `Name_of_PoliticalParty` VARCHAR(255),
    `Account_No` VARCHAR(20),
    `Prefix` VARCHAR(5),
    `Bond_Number` INT,
    `Denominations` INT,
    `Pay_Branch_Code` VARCHAR(20),
    `Pay_Teller` INT
);
"""
cursor.execute(create_table_query)

# Open the CSV file and process each line
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)  # Skip header if present

    for row in csv_reader:
        sr_no, date_encashment, party_name, account_no, prefix, bond_number, denominations, branch_code, teller = row
        
        sql_date_encashment=convert_to_mysql_date(date_encashment)

        insert_query = f"""
        INSERT INTO {table_name} (`Sr_No`, `Date_of_Encashment`, 
                `Name_of_PoliticalParty`, `Account_No`, 
                `Prefix`, `Bond_Number`, `Denominations`, 
                `Pay_Branch_Code`, `Pay_Teller`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
                sr_no, sql_date_encashment, 
                party_name, account_no, 
                prefix,int(bond_number.replace('"', '').replace(',', '')),  # Convert bond_number to int
                int(denominations.replace(',', '')), 
                branch_code, int(teller)
            )
        
        cursor.execute(insert_query, values)

        connection.commit()  # Commit each successful insert or update

# Close cursor and connection
cursor.close()
connection.close()

print(f"Data from '{csv_file_path}' uploaded/updated to '{table_name}' in MySQL")
