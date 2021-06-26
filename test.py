import mysql.connector,search, csv

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="CSE308"
	)

mycursor = mydb.cursor()


file = csv.DictReader(open("2016_Data_Post_Preprocess.csv", newline=''))
a,b,c,d,e,f,g = 0,0,0,0,0,0,0
for x in file:
	a += int(x['White'])
	b += int(x['Black'])
	c += int(x['Latino'])
	d += int(x['Democrat'])
	e += int(x['Republican'])
	f += int(x['Libertarian'])
	g += int(x['Green'])

print(a,b,c,d,e,f,g)

'''
Questions for professor:
- Data sources (only one set rt now)
- Exact meaning of majority-minority input
  - race percent >= input ||| party vote percent > input 
    - two separate percentage inputs?

-----------
- (partyvote/votingpop) vs (partyvote/totalpop)
--cosmetic	
	large integer: comma notation
	party: democratic (yes) democrat(no)
-percentage compared to whole state 
-----------
-- percentage: race threshold
-- ignore insignificant race
-- hispanic don't need to be separate catagory and do multiplication with race




'''