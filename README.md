# 23110335_DCC
Assignment 4

b. [3 Pts.]
**i. First, convert the PDF files to CSV using FITZ.** 
  Folder "pdf to csv" contains two python files which converts following conversion
    1) Election bond data related to party : from Party_data.pdf to output_party.csv
    2) Election bond data related to party : from Company_data.pdf to output_company.csv

  File : code_party_csv.py 
  This file will convert Party_data.pdf to output_party.csv

  File : code_company_csv.py
  This file will convert Company_data.pdf to output_company.csv

****ii.Then load these two different CSV files into two different tables in the database.**
**Folder Name : csv_to_mysql
File Name  : 1) code_sql_party_asn4.py
             2) code_sql_company_asn4.py**

Steps :
1) Before executing this two  files, create a database **"assgnment4"** using mysql command line.
2) Ensure both csv files in this folder
3) Execute code_sql_party_asn4.py to import party related date to mysql database **"assgnment4"**
   
   a)  This code will create table (party) using following query
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
  b)  Csv file is read and each row is imported in the table using following query. Dates read from the csv file is converted to mysql format using convert_to_mysql_date function.
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
          
5) Execute code_sql_company_asn4.py to import party related date to mysql database **"assgnment4"**

 a)  This code will create table (party) using following query
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
  b)  Csv file is read and each row is imported in the table using following query. Dates read from the csv file is converted to mysql format using convert_to_mysql_date function.
        insert_query = f"""
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
6) adf



  
  

    
  
