import shapely, fiona, csv

# id, location name, population, 6 races + hispanic

# hispanic: yes / no /  doesn't matter
# include hispanic as default, calculate non-hispanic by subtraction
# 2016 presidental election
def passCond(x):
	return x['TOTPOP']==0


with open('2016_Data_Post_Preprocess.csv', mode='w') as csv_file:
	fieldnames = ['ID','County', 'Jurisdiction', 'Precinct', 
	'Population', 'White', 'Black','Native', 'Asian', 'Island', 'Other', 'Multi',
	'H_Population', 'H_White', 'H_Black', 'H_Native', 'H_Asian', 'H_Island', 'H_Other', 'H_Multi',
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
					'Population': y['TOTPOP'], 'H_Population': y['HISP'] ,
					'White': y['NH_WHITE']+y['H_WHITE'], 'H_White': y['H_WHITE'], 
					'Black': y['NH_BLACK']+y['H_BLACK'], 'H_Black': y['H_BLACK'], 
					'Native': y['NH_AMIN']+y['H_AMIN'],  'H_Native': y['H_AMIN'], 
					'Asian': y['NH_ASIAN']+y['H_ASIAN'], 'H_Asian': y['H_ASIAN'], 
					'Island': y['NH_NHPI']+y['H_NHPI'], 'H_Island': y['H_NHPI'], 
					'Other': y['NH_OTHER']++y['H_OTHER'], 'H_Other': y['H_OTHER'], 
					'Multi': y['NH_2MORE']+y['H_2MORE'],'H_Multi': y['H_2MORE'],
					'Democrat': y['PRES16D'], 'Republican': y['PRES16R'], 'Libertarian': y['PRES16L'], 'Green': y['PRES16G']
					})

