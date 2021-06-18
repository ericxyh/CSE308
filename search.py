import csv, mysql.connector

# race in ['White','Black','Native','Asian','Island','Other']
# percent int between 50 and 100
# hispanicCheck None, True, or False
# Only Hispanic
# Only certain Race
# Both Hispanic/Race

def search(race, percent):
	file = csv.DictReader(open("2016_Data_Post_Preprocess.csv", newline=''))
	ans=[]
	for x in file:
		racePop=int(x[race])
		racePer = 100*racePop / int(x['Population'])
		if racePer>=percent:
			for y in ['Democrat','Republican','Libertarian','Green']:
				if int(x[y])/int(x['Population']) >= 0.5:
					ans.append([x['County'],x['Jurisdiction'],x['Precinct'],y])
					break
	ans.sort(reverse=True)
	return ans


#print(search('Black',50,False))
#print(searchHispanic(50))