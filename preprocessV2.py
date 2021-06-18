import mysql.connector, fiona, csv


'''
-'White', 'Black','Native', 'Asian', 'Island', 'Other', 'Multi'
v1: All types
v2: Non-hispanic only

'''

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="CSE308"
	)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS vote2016")
# location = county + jurisdiction + precinct
mycursor.execute("CREATE TABLE vote2016 (County VARCHAR(255), Jurisdiction VARCHAR(255), Precinct VARCHAR(255),"
	+"Population INT, White INT, Black INT,Native INT, Asian INT, Island INT, Other INT, Multi INT,"
	+"H_Population INT, H_White INT, H_Black INT, H_Native INT, H_Asian INT, H_Island INT, H_Other INT, H_Multi INT,"
	+"Democrat INT, Republican INT, Libertarian INT, Green INT,"+
	"PRIMARY KEY (County,Jurisdiction,Precinct))")

with fiona.open("MI/MI.shp",'r') as a:
	cmd = ("INSERT INTO vote2016 (County, Jurisdiction, Precinct, "+
		"Population, White, Black, Native, Asian, Island, Other, Multi,"+
		"H_Population, H_White, H_Black, H_Native, H_Asian, H_Island, H_Other, H_Multi,"+
		"Democrat, Republican, Libertarian, Green) "+
		"VALUES (%s,%s,%s,"+
		"%s,%s,%s,%s,%s,%s,%s,%s,"+
		"%s,%s,%s,%s,%s,%s,%s,%s,"+
		"%s,%s,%s,%s)")
	for x in a:
		y = x["properties"]
		if y['TOTPOP']==0:
			continue
		else:
			val = (y['county_nam'],y['jurisdic_1'],y['precinct'],
				y['TOTPOP'],y['NH_WHITE'],y['NH_BLACK'],y['NH_AMIN'],y['NH_ASIAN'],y['NH_NHPI'],y['NH_OTHER'],y['NH_2MORE'],
				y['HISP'],y['H_WHITE'],y['H_BLACK'],y['H_AMIN'],y['H_ASIAN'],y['H_NHPI'],y['H_OTHER'],y['H_2MORE'],
				y['PRES16D'],y['PRES16R'],y['PRES16L'],y['PRES16G'])
			mycursor.execute(cmd,val)

mydb.commit()
mycursor.close()
mydb.close()











