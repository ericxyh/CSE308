import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password=""
	)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

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