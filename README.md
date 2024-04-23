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
4) Execute code_sql_company_asn4.py to import party related date to mysql database **"assgnment4"**



  
  

    
  
