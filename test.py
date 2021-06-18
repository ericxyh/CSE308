import mysql.connector,search

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="CSE308"
	)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")


print(search.search('White',50))

'''
Questions for professor:
- Data sources (only one set rt now)
- Exact meaning of majority-minority input
  - race percent >= input ||| party vote percent > input 
    - two separate percentage inputs?


- (partyvote/votingpop) vs (partyvote/totalpop)
- only hispanic case
- min percentage(?) and cases that are insignificant(asian, other, black+hispanic)



-- percentage: race threshold
-- ignore insignificant race
-- hispanic don't need to be separate catagory and do multiplication with race




'''