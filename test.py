import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="CSE308"
	)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS vote2016")
# location = county + jurisdiction + precinct
mycursor.execute("CREATE TABLE vote2016 (Location VARCHAR(255) PRIMARY KEY,"
	+"Population INT, White INT, Black INT,Native INT, Asian INT, Island INT, Other INT, Multi INT,"
	+"H_Population INT, H_White INT, H_Black INT, H_Native INT, H_Asian INT, H_Island INT, H_Other INT, H_Multi INT,"
	+"Democrat INT, Republican INT, Libertarian INT, Green INT)")

mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x)


'''
Questions for professor:
- Data sources (only one set rt now)
- Database(?)
- Exact meaning of majority-minority
- (partyvote/votingpop) vs (partyvote/totalpop)
- only hispanic case
- min percentage(?) and cases that are insignificant(asian, other, black+hispanic)
'''