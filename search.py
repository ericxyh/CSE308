import csv, mysql.connector

# race in ['White','Black','Native','Asian','Island','Other']
# percent int between 50 and 100
# hispanicCheck None, True, or False
# Only Hispanic
# Only certain Race
# Both Hispanic/Race

def search(race, percent, hispanicCheck):
	file = csv.DictReader(open("2016_Data_Post_Preprocess.csv", newline=''))
	ans=[]
	for x in file:
		racePop=0
		if hispanicCheck is None:
			racePop=int(x[race])
		elif hispanicCheck:
			racePop=int(x['H_'+race])
		else:
			racePop=int(x[race])-int(x['H_'+race])
		racePer = 100*racePop / int(x['Population'])
		if racePer>=percent:
			for y in ['Democrat','Republican','Libertarian','Green']:
				if int(x[y])/int(x['Population']) >= 0.5:
					ans.append([x['County'],x['Jurisdiction'],x['Precinct']])
					break
	ans.sort(reverse=True)
	return ans

def searchHispanic(percent):
	file = csv.DictReader(open("2016_Data_Post_Preprocess.csv", newline=''))
	ans=[]
	for x in file:
		if 100*int(x['H_Population'])/int(x['Population']) >= percent:
			ans.append((x['County']+'|'+x['Jurisdiction']+'|'+x['Precinct']))
	return ans

#print(search('Black',50,False))
#print(searchHispanic(50))