# Implementation of interactive website to access data in a well visualized form


###Tasks Perfomed

Project Implementation: Electoral Bonds Data Analysis and Visualization

1. PDF to Database Conversion

a. Loading PDF Files into Database Tables
	•	Files Processed:
	•	Details of Electoral Bonds submitted by SBI on 21st March 2024 (EB_Redemption_Details): Bonds encashed by political parties.
	•	Details of Electoral Bonds submitted by SBI on 21st March 2024 (EB_Purchase_Details): Bonds purchased by Individuals and Companies.

b. Steps for Processing:
	1.	PDF to CSV Conversion:
	•	Utilized fitz (PyMuPDF) for converting the PDF files into CSV format.
	•	Applied necessary preprocessing to ensure data integrity and proper formatting before saving as CSV.
	2.	Loading CSV into Database:
	•	Loaded the processed CSV files into two separate tables in a relational database.
	•	Table 1: EB_Redemption_Details
	•	Table 2: EB_Purchase_Details

2. Frontend Development

c. Creating the Frontend
	•	Developed a frontend using:
	•	Flask: Backend framework for handling requests and rendering templates.
	•	Bootstrap: For responsive and aesthetic web design.
	•	CSS & JavaScript: For custom styling and interactive functionalities.

d. Connecting Frontend to Database
	•	Established a connection between the frontend and the database to fetch and display data dynamically, as covered in the special class.

3. Web Design Features

e. Implemented Features:
	1.	Search Functionality:
	•	Users can search for specific records based on Bond Number or filter data on columns like date, political party, or company name.
	•	Search results are displayed in a dynamically fetched table from the database.
	2.	Dropdown/Search Options:
	•	Select a Company/Individual from a dropdown/search to view the total number of bonds and their value purchased per year. Results are visualized in a bar plot.
	•	Select a political party to view the total number of bonds and their value per year. Results are visualized in a bar plot.
	3.	Donation Insights:
	•	Option to select a political party and see which companies have donated to it and the amounts (individually and combined).
	•	Option to select a company and view the political parties they have donated to and the amounts (individually and combined).
	4.	Data Visualization:
	•	Provided a pie chart depicting the total amount of donations to all parties.
	5.	Plot Export Functionality:
	•	Added functionality to save displayed plots in formats like PNG/JPEG.
	6.	Additional Plots:
	•	Created and showcased various plots such as Pie charts, Bar charts, and Line charts using ChartJS to visualize data insights.
	•	For complex relationships, used Alluvial diagrams in sections 1e4 and 1e5.

f. Additional Features:
	•	Developed a unique plot using ChartJS that adds a fresh perspective to the data visualization, earning bonus points.

	•	A comprehensive README file with instructions on how to set up the website locally and documentation of all implemented features.

This README serves as a detailed implementation guide for the project, showcasing the steps taken from data processing to web application development, culminating in a robust data analysis and visualization tool.


####Implemenation

**1. b**
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
                  
                  
                  
**1. c. : Create a frontend using FLASK, Bootstrap, CSS, Javascript, etc following the web design instructions**
		
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

**1. d. : Connect the front end to the database**

	1) In the main.py file, following are used to configure application for data base connection
 		
   			from flask_mysqldb import MySQL
	
			app = Flask(__name__)
			app.config['MYSQL_HOST'] = 'localhost'
			app.config['MYSQL_USER'] = 'root'
			app.config['MYSQL_PASSWORD'] = 'Sqllinux68'
			app.config['MYSQL_DB'] = 'assgnment4'
			
			mysql = MySQL(app)

	2)  Following functions are used to establish connecting and get data from database

		 	cursor=mysql.connection.cursor()
			cursor.execute("SELECT DISTINCT `Name_of_PoliticalParty` FROM party")
			data = cursor.fetchall()
	  		cursor.close()

**1. e.**
  ****1.e.i. Search for Party related bonds search and company related bond search**

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
 
![search page](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/c3cdfe83-5210-4f0c-bea6-bf5c713dff0b)
 

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



**1. e.**


  **1.e.2. The option to select a Company/Individual from a drop-down/search**
  
  **a) WEB INTERFACE for Year Wise  Election Bond Details for purchaser (company/indivisual)**

  	1) Following image shows the web interface for selecting company name and showing result for 1.e.2

 ![company_wise_bond_details](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/dd57282b-747f-40b7-bd1e-d589f6d9aab8)

 **b) RESULT for Year Wise  Election Bond Details for purchaser (company/indivisual)**
  		(1) Drop down menu used for searching and selecting compnay name.
   		(2) At a time only one company can be selected. 
    		(3) When user click "Year Wise Bond Details" button, request to server is sent with company name.
     		(4) company_bond_count() function is called. 
      		(5) Different query is executed and result is shown by using ie2_company.html
    
    		"SELECT DISTINCT `Name_of_Purchaser` FROM `company`
		"SELECT COUNT(*) FROM company where `Name_of_Purchaser`=%s",(selected_option,)) 	
   		("SELECT YEAR(`Date_of_Purchase`) as year, COUNT(*) as count,SUM(`Denominations`) as total_amount from company where `Name_of_Purchaser`=%s group by YEAR(`Date_of_Purchase`)",(selected_option,)); 


 **c) RESULT IMAGE**
      		
![compnay  year wise with pie chart1](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/cc5eb330-8106-4c72-8a21-5ec141b5b868)




**1. e.**


  **1.e.3. The option to select a Company/Individual from a drop-down/search and show year wise result**
  
  **a) WEB INTERFACE for Year Wise  Election Bond Details for purchaser (company/indivisual)**

  	1) Following image shows the web interface for selecting Party name and showing result for 1.e.3

   ![party_wise_webinterface](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/da166954-0e41-4c01-957f-604d7dd868dd)


  
  **b) Result 1.e.3 and 1.e.6**
  	(1) Drop down menu used for searching and selecting party name.
    	(2) At a time only one party can be selected.
      	(3) When user click "yearwise bond details", request to server is sent with party name.
	(4) def count_party_bond():() function is called. 
  	(5) Inside this function, different query is executed and result is shown by using 1e3_party_bond.html
    	(6) Following queries are executed and result is shown year wise.

	 	SELECT DISTINCT `Name_of_PoliticalParty` FROM party
    		SELECT COUNT(*) FROM `party` WHERE `Name_of_PoliticalParty`=%s",(selected_option,)
       		SELECT YEAR(`Date_of_Encashment`) as year, COUNT(*) as count,SUM(`Denominations`) as total_amount from party where `Name_of_PoliticalParty`=%s group by YEAR(`Date_of_Encashment`)",(selected_option,)


**c) RESULT IMAGE**

      
![party_yearwise_result](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/51c3b047-6c97-4f3c-911d-0d63168c8c2f)


**1.e.4 Similarly, provide an option to select a company from a drop-down/search, showcasing which parties they have donated and what amount individually and combined**
 
 
 **a) WEB INTERFACE for for party with company wise  Election Bond Details**

  	1) Following image shows the web interface for selecting Party name 

   ![party_wise_webinterface](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/da166954-0e41-4c01-957f-604d7dd868dd)

 
  **b) Result 1.e.4 and 1.e.6**
  		(1) Drop down menu used for searching and selecting party name.
		(2) At a time only one party can be selected.
  		(3) When user click "yearwise bond details", request to server is sent with party name.
		(4) def count_party_bond():() function is called. 
  		(5) Inside this function, different query is executed and result is shown by using 1e3_party_bond.html
    		(6) Following queries are executed and result is shown year wise.

	 		SELECT DISTINCT `Name_of_PoliticalParty` FROM party
    			SELECT COUNT(*) FROM `party` WHERE `Name_of_PoliticalParty`=%s",(selected_option,)
       			select bonds.purchaser, SUM(bonds.rs) as total from (SELECT company.Name_of_Purchaser as purchaser, company.Denominations as rs, company.Bond_Number as bn from company INNER JOIN party ON company.Bond_Number=party.Bond_Number WHERE party.Name_of_PoliticalParty=%s) bonds GROUP by bonds.purchaser",(selected_option,));
	

   		7)  Result and pie chart is showing on the same page

**c) RESULT IMAGE**

![party_companywise_result](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/db07c758-6732-4728-819e-c3eae5957e00)





**1.e.5 Similarly, provide an option to select a company from a drop-down/search, showcasing which parties they have donated and what amount individually and combined**


 **a) WEB INTERFACE for for company with party wise Election Bond Details**
		 1) Following image shows the web interface for selecting Party name 
 

![company_wise_bond_details](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/dd57282b-747f-40b7-bd1e-d589f6d9aab8)
 
 **b) Result 1.e.5**
 		(1)  Drop down menu used for searching and selecting compnay name. 
   		(2) At a time only one company can be selected.
     		(3) When user click button "party wise bond details" , request to server is sent with company name. 
       		(4) company_bond_count() function is called. 
	 	(5)  Inside this function, different query is executed and result is shown by using ie2_company.html
   		
     			SELECT DISTINCT `Name_of_Purchaser` FROM `company` 
			SELECT COUNT(*) FROM company where `Name_of_Purchaser`=%s",(selected_option,)
			SELECT DISTINCT bonds.party_name, SUM(bonds.rs) from (SELECT party.Name_of_PoliticalParty as party_name, party.Denominations as rs, party.Bond_Number as bn from party INNER JOIN company ON company.Bond_Number=party.Bond_Number WHERE company.Name_of_Purchaser=%s) bonds GROUP BY bonds.party_name",(selected_option,)
 		
		(6)  Result and pie chart is showing on the same page.

**c) RESULT IMAGE**
  ![company_partywise_result](https://github.com/TejasLohia21/23110335_DCC/assets/143334144/5df30da2-d99d-4072-a6e3-4000f8bd2839)

  
 **1.e.6 Pie Chart**
 	Ref. 1.e.2,1.e.3,1.e.4,1.e.5
  	Pie Chart has been shown along with above result (1.e.2,1.e.3,1.e.4,1.e.5)


**2. Plots:**
			(1)	ChartJS has been used in all above html files for ploting the graph
  			(2)	Script file included in the html file
    						<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>

 			(3)	Following is used for pie chart/pie (type bar/pie)

		      			new Chart(ctx, {
					type: 'bar',
				    	data: {
					    	labels: xValues,
					      	datasets: [{
							label: 'Year Wise Bond',
							backgroundColor:colors,
							borderColor: "#FFFFFF",
							data: yValues,
							borderWidth: 1
					      	}]
				    	},
				    	options: {
		        			scales: {
		            			yAxes: [{
		                			ticks: {
				            			beginAtZero: true,
				            			suggestedMax: 15 // Set the maximum height of the chart to 20
				        		}
		            				}]
		        			}
		    			}
				    
					});


     					new Chart(document.getElementById("div_party_vs_amount_pie_chart"), {
							type: 'pie',
							data: {
				            			labels: xValues,
				            			datasets: [{
									label: "Party Wise Bond",
									backgroundColor:colors,
				                			data: yValues
				            			}]
				        		},
							options: {
								title: {
									display: true,
									text: 'Party Wise Bond'
								}
					
							}
						}
						);
		

  
    
**3. Extra Features**
			(1) In search program, different type of combination of search is implemented.
   			(2) For company search, follwing fields in different combination can be used
      					(a) Name of Purchaseer
	   				(b) Bond No
					(c) Denomination
     					(d) Issue Branch Code
	  				(e) Year of issue
       					(d) Ref No URN
	    		(3) For party search, follwing fields in different combination can be used
       					(a) Name of Party
	   				(b) Bond No
					(c) Denomination
     					(d) Issue Branch Code
	  				(e) Year of issue

**4. Readme**
		(1) Readme with result of 1.e has been shown.
  		(2) pip files required to install : flask flask-mysqldb json
	 	(3) Port number and IP address can be specified in main.py
   			app.run(host="0.0.0.0", port="8900", debug = True) 
      		(4) Following command is used to start server
    					python3 main.py
      
      					


**5. Reference**
			(1)   https://flask.palletsprojects.com/en/3.0.x/quickstart/
   			(2)   https://www.w3schools.com/bootstrap/bootstrap_forms.asp
      			(3)   https://www.w3schools.com/bootstrap/bootstrap_grid_basic.asp
	 		(4)   https://getbootstrap.com/docs/4.1/components/forms/
    			(5)   https://codepen.io/BillDou/pen/oNoGBXb
       			(6)   https://github.com/PatidarRitesh/Flask_App_Demo/tree/main
	  		(7)   Class Excercise
    
   

       
