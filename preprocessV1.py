import shapely, fiona, csv

# id, location name, population, 6 races + hispanic

# hispanic: yes / no /  doesn't matter
# include hispanic as default, calculate non-hispanic by subtraction
# 2016 presidental election
def passCond(x):
	return x['TOTPOP']==0


with open('2016_Data_Post_Preprocess.csv', mode='w') as csv_file:
	fieldnames = ['ID','County', 'Jurisdiction', 'Precinct', 
	'Population', 'White', 'Black','Latino',
	'Democrat', 'Republican', 'Libertarian', 'Green']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	with fiona.open("MI/MI.shp",'r') as a:
		for x in a:
			y = x["properties"]
			if passCond(y):
				continue
			else:
				writer.writerow({'County': y["county_nam"], 'Jurisdiction': y["jurisdic_1"], 'Precinct': y["precinct"], 'ID': y["VTD"], 
					'Population': y['TOTPOP'], 'Latino': y['HISP'] ,
					'White': y['NH_WHITE']+y['H_WHITE'], 'Black': y['NH_BLACK']+y['H_BLACK'], 
					'Democrat': y['PRES16D'], 'Republican': y['PRES16R'], 'Libertarian': y['PRES16L'], 'Green': y['PRES16G']
					})

