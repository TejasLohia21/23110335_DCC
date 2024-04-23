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
'''
def convert_to_integer(number_string):
    # Remove commas from the number string
    number_string_without_commas = number_string.replace(',', '')

    # Convert the string to an integer
    number = int(number_string_without_commas)
    return number
'''
table_name = 'company'
csv_file_path = 'output_company.csv'

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
    `Ref_No_URN` VARCHAR(50),
    `Date_of_Journal` DATE,
    `Date_of_Purchase` DATE,
    `Date_of_Expiry` DATE,
    `Name_of_Purchaser` VARCHAR(255),
    `Prefix` VARCHAR(10),
    `Bond_Number` INT,
    `Denominations` INT,
    `Issue_Branch_Code` INT,
    `Issue_Teller` INT,
    `Status` VARCHAR(20)
);
"""
cursor.execute(create_table_query)

# Open CSV file and process each line
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)  # Skip header if present

    for row in csv_reader:
        sr_no, reference_no, journal_date, purchase_date, expiry_date, purchaser_name, prefix, bond_number, denominations, branch_code, teller, status = row
        
        sql_journal_date=convert_to_mysql_date(journal_date)
        sql_purchase_date=convert_to_mysql_date(purchase_date)
        sql_expiry_date=convert_to_mysql_date(expiry_date)
        #int_denominations=convert_to_integer(denominations)

        # Prepare SQL INSERT statement with backticks around column names
        sql = f"""
        	INSERT INTO {table_name} (`Sr_No`,`Ref_No_URN`,`Date_of_Journal`,`Date_of_Purchase`,`Date_of_Expiry`,
    		`Name_of_Purchaser`,`Prefix`,`Bond_Number`,`Denominations`,`Issue_Branch_Code`,`Issue_Teller`,`Status`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            sr_no, reference_no, sql_journal_date,sql_purchase_date,
            sql_expiry_date, purchaser_name, prefix, int(bond_number.replace('"', '').replace(',', '')),  # Convert bond_number to int
            int(denominations.replace(',', '')) , int(branch_code), int(teller), status
        )

        # Execute the SQL INSERT statement with the values
        cursor.execute(sql, values)

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()

print(f"Data from '{csv_file_path}' uploaded to '{table_name}' in MySQL")
