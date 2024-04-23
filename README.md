# 23110335_DCC
Assignment 4

**1. b. [3 Pts.]**
  **1.b.i. First, convert the PDF files to CSV using FITZ.** 
        Folder "pdf to csv" contains two python files which converts following conversion
          1) Election bond data related to party : from Party_data.pdf to output_party.csv
          2) Election bond data related to party : from Company_data.pdf to output_company.csv
      
        File : code_party_csv.py 
        This file will convert Party_data.pdf to output_party.csv
      
        File : code_company_csv.py
        This file will convert Company_data.pdf to output_company.csv

  **1.b.ii.Then load these two different CSV files into two different tables in the database.**
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
                            
                  5) Execute code_sql_company_asn4.py to import company related date to mysql database **"assgnment4"**
                  
                   a)  This code will create table (company) using following query
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
                  
                  
                  
**1. c.** : Create a frontend using FLASK, Bootstrap, CSS, Javascript, etc following the web design instructions
            Folder name : electoral_bond
                          a)  This folder contains flask application with template folder.
                          b)  Template folder contains all html files
            File :  main.py is main applicatoin which is routing all incoming request from client web browser.
            Javascript, bootstrap and css are embedded in the each html file   

                      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
                      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                      <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>
          **1.e.1**
          @app.route('/search')	
                   def search():
	                  render_template('bond_search.html')
          @app.route('/search/result_party',methods = ["POST", "GET"])	
                   def search_result_party():
                   return(render_template('bond_search.html',show_flag=show_flag,total_len=len(data),data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year))

        @app.route('/search/result_company',methods = ["POST", "GET"])	
        def search_result_company():
        return(render_template('bond_search.html',show_flag=show_flag,total_len=len(data),data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year,urn=urn))
   

@app.route('/search/result_party',methods = ["POST", "GET"])	
def search_result_party():

**1. e.**
  **1.e.i. Search for Party related bonds search and company related bond search

		@app.route('/search')	
                	def search():
	                render_template('bond_search.html')
          	@app.route('/search/result_party',methods = ["POST", "GET"])	
                	def search_result_party():
                render_template('bond_search.html',show_flag=show_flag,total_len=len(data),data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year))

        	@app.route('/search/result_company',methods = ["POST", "GET"])	
        		def search_result_company():
	  		     return(render_template('bond_search.html',show_flag=show_flag,total_len=len(data),data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year,urn=urn))
   
	a)  bond search.html will display following page

 ![search_page](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/f1dc08d2-1efc-40c9-8943-cd2dc3907729)

 	b) Two types of search is implemented.
  		i) 	Party wise electoral bonds data : Search can be made using party name, bond number, Denominations, Year of encashment, branch code
    		ii)	Company wise electoral bonds data : Search can be made using purchaser, bond number, Denominations, Year of encashment, branch code and urn number

	Result :
 	i)   Following image shows the result of search for bond nummber 4276.
  		
  ![party_search_bondno](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/97539fc1-c316-47ad-a6ed-a12cd296d5f5)

  	      Above search will result in following query for table.

  	ii)  Following image shows the result of search for party name "shivsena" and year 2019. Total results are 125. But webpage shows first 10 results.
   ![search_shivsena_year2019](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/6c13d711-37f5-48d7-97cd-fa808f41aa10)

	     Following SQL QUERY is generated
      		SELECT * FROM party WHERE `Name_of_PoliticalParty` LIKE "%shivsena%" AND YEAR(`Date_of_Encashment`) = 2019
   
         iii)  Following image shows the result of 
	 	a) Name of purchaser : "A B C INDIA LIMITED"
   		b) Denominations     :   1000000
![company_search_A B C INDIA LIMITED_Debinubatuibs_1000000 png](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/7ce8a032-95de-4065-a14a-bc475b130a2a)

	Following query is generated for above result
 	SELECT * FROM company WHERE `Name_of_Purchaser` LIKE "%A B C INDIA LIMITED%" AND `Denominations` = 1000000

  


   

      		
      	

  


  

    
  
