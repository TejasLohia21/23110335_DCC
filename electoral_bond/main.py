from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL
import json
import random


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mayurt'
app.config['MYSQL_DB'] = 'assgnment4'

mysql = MySQL(app)



def render_party_yearwise_bond(selected_option):
	cursor=mysql.connection.cursor()
	cursor.execute("SELECT DISTINCT `Name_of_PoliticalParty` FROM party")
	data = cursor.fetchall()
	
	#cursor.execute("SELECT COUNT(*) FROM `party` WHERE `Name_of_PoliticalParty`=%s",("SHIVSENA",)) 
	cursor.execute("SELECT COUNT(*) FROM `party` WHERE `Name_of_PoliticalParty`=%s",(selected_option,)) 
	bond_count = cursor.fetchall()
	
	cursor.execute("SELECT YEAR(`Date_of_Encashment`) as year, COUNT(*) as count,SUM(`Denominations`) as total_amount from party where `Name_of_PoliticalParty`=%s group by YEAR(`Date_of_Encashment`)",(selected_option,)); 
	yearwise_bond = cursor.fetchall()
	print(yearwise_bond)
	
	arr1 = [] #year
	arr2 = [] #bond
	arr3 = [] #amt
	for i in range(len(yearwise_bond)):
		arr1.append(yearwise_bond[i][0])
		arr2.append(yearwise_bond[i][1])
		arr3.append(int(yearwise_bond[i][2]))
	
	#print("arr1 ",arr1)
	#print("arr2", arr2)
	#print("arr3", arr3)
	cursor.execute("SELECT SUM(`Denominations`) FROM `party` WHERE `Name_of_PoliticalParty`=%s",(selected_option,)) 
	tot=cursor.fetchall()
	total_sum=int(tot[0][0])
	print(total_sum)
	
	cursor.close()
	return render_template("1e3_party_bond.html",party_name = data,year_wise_bond=1,party_bond_count=bond_count,selected_party=selected_option,years = json.dumps(arr1),no_of_bonds_per_year = json.dumps(arr2),amounts_per_year=json.dumps(arr3),total_sum=total_sum)


def render_party_companywise_bond(selected_option):
	cursor=mysql.connection.cursor()
	cursor.execute("SELECT DISTINCT `Name_of_PoliticalParty` FROM party")
	data = cursor.fetchall()
	
	#cursor.execute("SELECT COUNT(*) FROM `party` WHERE `Name_of_PoliticalParty`=%s",("SHIVSENA",)) 
	cursor.execute("SELECT COUNT(*) FROM `party` WHERE `Name_of_PoliticalParty`=%s",(selected_option,)) 
	bond_count = cursor.fetchall()
	
	cursor.execute("select bonds.purchaser, SUM(bonds.rs) as total from (SELECT company.Name_of_Purchaser as purchaser, company.Denominations as rs, company.Bond_Number as bn from company INNER JOIN party ON company.Bond_Number=party.Bond_Number WHERE party.Name_of_PoliticalParty=%s) bonds GROUP by bonds.purchaser",(selected_option,));
	
	#cursor.execute("SELECT YEAR(`Date_of_Encashment`) as year, COUNT(*) as count,SUM(`Denominations`) as total_amount from party where `Name_of_PoliticalParty`=%s group by YEAR(`Date_of_Encashment`)",(selected_option,)); 

	yearwise_bond = cursor.fetchall()
	print(yearwise_bond)
	
	arr1 = [] #year
	arr2 = [] #bond
	arr3 = [] #amt
	for i in range(len(yearwise_bond)):
		print(i)
		arr1.append(yearwise_bond[i][0])
		arr2.append(int(yearwise_bond[i][1]))
		#arr3.append(int(yearwise_bond[i][2]))
	
	#print("arr1 ",arr1)
	#print("arr2", arr2)
	#print("arr3", arr3)
	cursor.execute("SELECT SUM(`Denominations`) FROM `party` WHERE `Name_of_PoliticalParty`=%s",(selected_option,)) 
	tot=cursor.fetchall()
	total_sum=int(tot[0][0])
	print(total_sum)
	
	cursor.close()
	return render_template("1e3_party_bond.html",party_name = data,company_wise_bond=1,party_bond_count=bond_count,selected_party=selected_option,company_name = json.dumps(arr1),amount = json.dumps(arr2),total_sum=total_sum)


def render_company_yearwise_bond(selected_option):
	print("company year wise")
	cursor=mysql.connection.cursor()
	cursor.execute("SELECT DISTINCT `Name_of_Purchaser` FROM `company` ")
	data = cursor.fetchall()
	
	cursor.execute("SELECT COUNT(*) FROM company where `Name_of_Purchaser`=%s",(selected_option,)) 
	total_bond_count = cursor.fetchall()
	
	cursor.execute("SELECT YEAR(`Date_of_Purchase`) as year, COUNT(*) as count,SUM(`Denominations`) as total_amount from company where `Name_of_Purchaser`=%s group by YEAR(`Date_of_Purchase`)",(selected_option,)); 
	yearwise_bond = cursor.fetchall()
	print(yearwise_bond)
	
	arr1 = [] #year
	arr2 = [] #bond
	arr3 = [] #amt
	for i in range(len(yearwise_bond)):
		arr1.append(yearwise_bond[i][0])
		arr2.append(yearwise_bond[i][1])
		arr3.append(int(yearwise_bond[i][2]))
	
	#print("arr1 ",arr1)
	#print("arr2", arr2)
	#print("arr3", arr3)
	cursor.execute("SELECT SUM(`Denominations`) FROM `company` WHERE `Name_of_Purchaser`=%s",(selected_option,)) 
	tot=cursor.fetchall()
	total_sum=int(tot[0][0])
	print(total_sum)
	
	cursor.close()
	return render_template("ie2_company.html",company_name = data,year_wise_bond=1,company_bond_count=total_bond_count,selected_company=selected_option,years = json.dumps(arr1),no_of_bonds_per_year = json.dumps(arr2),amounts_per_year=json.dumps(arr3),total_sum=total_sum)


def render_company_partywise_bond(selected_option):
	print("company PARTY wise")
	cursor=mysql.connection.cursor()
	cursor.execute("SELECT DISTINCT `Name_of_Purchaser` FROM `company` ")
	data = cursor.fetchall()
	
	cursor.execute("SELECT COUNT(*) FROM company where `Name_of_Purchaser`=%s",(selected_option,)) 
	bond_count = cursor.fetchall()

	cursor.execute("SELECT DISTINCT bonds.party_name, SUM(bonds.rs) from (SELECT party.Name_of_PoliticalParty as party_name, party.Denominations as rs, party.Bond_Number as bn from party INNER JOIN company ON company.Bond_Number=party.Bond_Number WHERE company.Name_of_Purchaser=%s) bonds GROUP BY bonds.party_name",(selected_option,))
	#cursor.execute("select bonds.purchaser, SUM(bonds.rs) as total from (SELECT company.Name_of_Purchaser as purchaser, company.Denominations as rs, company.Bond_Number as bn from company INNER JOIN party ON company.Bond_Number=party.Bond_Number WHERE party.Name_of_PoliticalParty=%s) bonds GROUP by bonds.purchaser",(selected_option,));
	
	yearwise_bond = cursor.fetchall()
	print(yearwise_bond)
	
	arr1 = [] #year
	arr2 = [] #bond
	arr3 = [] #amt
	for i in range(len(yearwise_bond)):
		print(i)
		arr1.append(yearwise_bond[i][0])
		arr2.append(int(yearwise_bond[i][1]))
		#arr3.append(int(yearwise_bond[i][2]))
	
	print("arr1 ",arr1)
	print("arr2", arr2)
	#print("arr3", arr3)
	print(len(arr1))
	
	cursor.execute("SELECT SUM(`Denominations`) FROM `company` WHERE `Name_of_Purchaser`=%s",(selected_option,)) 
	tot=cursor.fetchall()
	total_sum=int(tot[0][0])
	print(total_sum)

	cursor.close()

	return render_template("ie2_company.html",company_name = data,party_wise_bond=1,company_bond_count=bond_count,selected_company=selected_option,party_name = json.dumps(arr1),amount = json.dumps(arr2),total_sum=total_sum)




@app.route('/')
def main_page():
	return render_template("index.html")
	
@app.route('/search')	
def search():
	print("search")
	return render_template('bond_search.html')

@app.route('/search/result_party',methods = ["POST", "GET"])	
def search_result_party():
	print("search_result")
	print(request.form)
	print(request.method)
	if request.method == "POST":
		print("search result post")
		party_name = request.form["party_name"]
		print(len(party_name))
		and_flag=0

		se=''
		if party_name != '':
			#print(party_name)
			se="`Name_of_PoliticalParty` LIKE " + "\"%" +party_name + "%\""
			print(se)    
	    		#search_term="Name_of_PoliticalParty LIKE " + party_name
			and_flag = 1
		
		bond_no = request.form["bond_number"]
		if bond_no != '':
			#print(int(bond_no))
			if and_flag == 1:
				se=se+" AND `Bond_Number` = " + bond_no
			else:
				se=se+" `Bond_Number` = " + bond_no	
				and_flag=1
				
		#print(se)

		denominations=request.form["denominations"]
		if denominations != '':
			#print(int(denominations))
			if and_flag == 1:
				se=se+" AND `Denominations` = " + denominations
			else:
				se=se+" `Denominations` = " + denominations	
				and_flag=1
				
		#print(se)

		pay_branch_code=request.form["pay_branch_code"]
		if pay_branch_code != '':
			#print(int(pay_branch_code))
			if and_flag == 1:
				se=se+" AND `Pay_Branch_Code` LIKE " + "\"%" +pay_branch_code + "%\""
			else:
				se=se+" `Pay_Branch_Code` LIKE " + "\"%" +pay_branch_code + "%\""
				and_flag=1
				
		#print(se)

		bond_year=request.form["year"]
		if bond_year != '' and bond_year != "NOT SELECTED":
			#print(bond_year)
			print("year : "+bond_year)
			if and_flag == 1:
				se=se+" AND YEAR(`Date_of_Encashment`) = " + bond_year
			else:
				se=se+" YEAR(`Date_of_Encashment`) = " + bond_year	
				and_flag=1

		#print(bond_no)
		#else:
		#	s1="Name_of_PoliticalParty LIKE "+party_name 
	    	#	print(s1)
		show_flag=0
		if(se != ''):
			cursor=mysql.connection.cursor()
			query="SELECT * FROM party WHERE " + se
			print(query)
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
			print(len(data))
			if len(data) > 9:
				data_len=10
			else:
				data_len=len(data)
			print("data len " + str(data_len))
			if(data_len>0):
				show_flag=1
				party = [] #year
				bond_nos = [] #bond
				Denominations=[]
				branch=[]
				year=[]
				for i in range(data_len):
					party.append(data[i][2])
					bond_nos.append(data[i][5])
					Denominations.append(data[i][6])
					branch.append(data[i][7])
					year.append(data[i][1])

				print(len(party))
				#print(party)
				#return(render_template('bond_search.html',show_flag=show_flag,data_len=data_len,results=data))
	
				return(render_template('bond_search.html',show_flag=show_flag,total_len=len(data),data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year))
	
	return render_template('bond_search.html')

@app.route('/search/result_company',methods = ["POST", "GET"])	
def search_result_company():
	print("search_result")
	print(request.form)
	print(request.method)
	if request.method == "POST":
		print("search result post")
		purchaser_name = request.form["purchaser_name"]
		print(len(purchaser_name))
		and_flag=0

		se=''
		if purchaser_name != '':
			print(purchaser_name)
			se="`Name_of_Purchaser` LIKE " + "\"%" +purchaser_name + "%\""
			print(se)    
	    		#search_term="Name_of_PoliticalParty LIKE " + party_name
			and_flag = 1
		
		bond_no = request.form["bond_number"]
		if bond_no != '':
			#print(int(bond_no))
			if and_flag == 1:
				se=se+" AND `Bond_Number` = " + bond_no
			else:
				se=se+" `Bond_Number` = " + bond_no	
				and_flag=1
		
		denominations=request.form["denominations"]
		if denominations != '':
			#print(int(denominations))
			if and_flag == 1:
				se=se+" AND `Denominations` = " + denominations
			else:
				se=se+" `Denominations` = " + denominations	
				and_flag=1
				
		
		pay_branch_code=request.form["pay_branch_code"]
		if pay_branch_code != '':
			#print(int(pay_branch_code))
			if and_flag == 1:
				se=se+" AND `Issue_Branch_Code` LIKE " + "\"%" +pay_branch_code + "%\""
			else:
				se=se+" `Issue_Branch_Code` LIKE " + "\"%" +pay_branch_code + "%\""
				and_flag=1
				
		bond_year=request.form["year"]
		if bond_year != '' and bond_year != "NOT SELECTED":
			#print(bond_year)
			print("year : "+bond_year)
			if and_flag == 1:
				se=se+" AND YEAR(`Date_of_Purchase`) = " + bond_year
			else:
				se=se+" YEAR(`Date_of_Purchase`) = " + bond_year	
				and_flag=1

		ref_no_urn=request.form["ref_no_urn"]
		if ref_no_urn != '':
			#print(int(pay_branch_code))
			if and_flag == 1:
				se=se+" AND `Ref_No_URN` LIKE " + "\"%" +ref_no_urn + "%\""
			else:
				se=se+" `Ref_No_URN` LIKE " + "\"%" +ref_no_urn + "%\""
				and_flag=1

		print("Final : " + se)

		show_flag=0
		if(se != ''):
			cursor=mysql.connection.cursor()
			query="SELECT * FROM company WHERE " + se
			print(query)
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
			print(len(data))
			if len(data) > 9:
				data_len=10
			else:
				data_len=len(data)
			print("data len " + str(data_len))
			if(data_len>0):
				show_flag=2
				party = [] #year
				bond_nos = [] #bond
				Denominations=[]
				branch=[]
				year=[]
				urn=[]
				for i in range(data_len):
					party.append(data[i][5])
					bond_nos.append(data[i][7])
					Denominations.append(data[i][8])
					branch.append(data[i][9])
					year.append(data[i][3])
					urn.append(data[i][1])

				print(len(party))
				#print(party)
				#return(render_template('bond_search.html',show_flag=show_flag,data_len=data_len,results=data))
	
				return(render_template('bond_search.html',show_flag=show_flag,total_len=len(data),data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year,urn=urn))
	
	return render_template('bond_search.html')


@app.route('/search/result_company1',methods = ["POST", "GET"])	
def search_result_company1():
	print("search_result")
	print(request.form)
	print(request.method)
	if request.method == "POST":
		print("search result post")
		party_name = request.form["party_name"]
		print(len(party_name))
		and_flag=0

		se=''
		if party_name != '':
			#print(party_name)
			se="`Name_of_PoliticalParty` LIKE " + "\"%" +party_name + "%\""
			print(se)    
	    		#search_term="Name_of_PoliticalParty LIKE " + party_name
			and_flag = 1
		
		bond_no = request.form["bond_number"]
		if bond_no != '':
			#print(int(bond_no))
			if and_flag == 1:
				se=se+" AND `Bond_Number` = " + bond_no
			else:
				se=se+" `Bond_Number` = " + bond_no	
				and_flag=1
				
		#print(se)

		denominations=request.form["denominations"]
		if denominations != '':
			#print(int(denominations))
			if and_flag == 1:
				se=se+" AND `Denominations` = " + denominations
			else:
				se=se+" `Denominations` = " + denominations	
				and_flag=1
				
		#print(se)

		pay_branch_code=request.form["pay_branch_code"]
		if pay_branch_code != '':
			#print(int(pay_branch_code))
			if and_flag == 1:
				se=se+" AND `Pay_Branch_Code` LIKE " + "\"%" +pay_branch_code + "%\""
			else:
				se=se+" `Pay_Branch_Code` LIKE " + "\"%" +pay_branch_code + "%\""
				and_flag=1
				
		#print(se)

		bond_year=request.form["year"]
		if bond_year != '' and bond_year != "NOT SELECTED":
			#print(bond_year)
			print("year : "+bond_year)
			if and_flag == 1:
				se=se+" AND YEAR(`Date_of_Encashment`) = " + bond_year
			else:
				se=se+" YEAR(`Date_of_Encashment`) = " + bond_year	
				and_flag=1

		#print(bond_no)
		#else:
		#	s1="Name_of_PoliticalParty LIKE "+party_name 
	    	#	print(s1)
		show_flag=0
		if(se != ''):
			cursor=mysql.connection.cursor()
			query="SELECT * FROM party WHERE " + se
			print(query)
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
			print(len(data))
			if len(data) > 10:
				data_len=11
			else:
				data_len=len(data)
			print("data len " + str(data_len))
			if(data_len>0):
				show_flag=1
				party = [] #year
				bond_nos = [] #bond
				Denominations=[]
				branch=[]
				year=[]
				for i in range(data_len):
					party.append(data[i][2])
					bond_nos.append(data[i][5])
					Denominations.append(data[i][6])
					branch.append(data[i][7])
					year.append(data[i][1])

				print(len(party))
				print(party[1])
				#return(render_template('bond_search.html',show_flag=show_flag,data_len=data_len,results=data))
	
				return(render_template('bond_search.html',show_flag=show_flag,data_len=data_len,party_name=party,bondnos=bond_nos,Denominations=Denominations,branch=branch,year=year))
	
	return render_template('index.html')

	
@app.route('/party',methods = ["POST", "GET"])
def party():
	cursor=mysql.connection.cursor()
	cursor.execute("SELECT DISTINCT `Name_of_PoliticalParty` FROM party")
	data = cursor.fetchall()
	cursor.close()
	return render_template("1e3_party_bond.html",party_name = data)
	

@app.route('/party/party_bond_count',methods = ["POST", "GET"])
def count_party_bond():
	if request.method == "POST":
		#print("HI")
		#print(request.method)
		#print(request.form)
		selected_option = request.form['selected_party_name']
		selected_button = request.form['party_action']

		if selected_button == "Year Wise Bond Details":
			return(render_party_yearwise_bond(selected_option))
		else:
			return(render_party_companywise_bond(selected_option))
			#return "company wise"

		
@app.route('/company',methods = ["POST", "GET"])
def company():
	cursor=mysql.connection.cursor()
	cursor.execute("SELECT DISTINCT `Name_of_Purchaser` FROM `company` ")
	data = cursor.fetchall()
	cursor.close()
	selected_option="ACROPOLIS MAINTENANCE SERVICES PRIVATE LIMITED"
	return render_template("ie2_company.html",company_name = data,selected_company=selected_option)
	
	
@app.route('/company/company_bond_count',methods = ["POST", "GET"])
def company_bond_count():
	if request.method == "POST":
		print("HI")
		print(request.method)
		print(request.form)
		selected_option = request.form['selected_company_name']
		selected_button = request.form['company_action']

		if selected_button == "Year Wise Bond Details":
			return(render_company_yearwise_bond(selected_option))
		else:
			return(render_company_partywise_bond(selected_option))

		

	
	
if __name__ == '__main__':
   app.run(host="0.0.0.0", port="8900", debug = True) 	


