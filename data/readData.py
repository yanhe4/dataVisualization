lines = [line.rstrip("\n") for line in open('ProvinWage.csv')]
lines = lines[8:]

map_industry = {'Goods producing industries 7': 'Goods Producting', 
'Construction': 'Construction', 
'Manufacturing': 'Manufacturing', 
'Service producing industries 9': 'Service', 
'Transportation and warehousing': 'Transportation',
'Finance and insurance': 'Finance', 
'Professional, scientific and technical services': 'Technical Services', 
'Educational services': 'Education', 
'Health care and social assistance': 'Health Care',
'Arts, entertainment and recreation': 'Arts'}

provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', 'New Brunswick', 
'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', 'Alberta', 'British Columbia']
years=[2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
data = {2008:{}, 2009:{}, 2010:{}, 2011: {}, 2012: {},
2013: {}, 2014: {}, 2015: {}, 2016: {}, 2017:{}}
for year in data:
	for province in provinces:
		data[year][province] = {}

for line in lines:
	linelist = line.split(',')
	if len(linelist) == 101:
		curInd = linelist[0].replace('"', '')
		if curInd in map_industry:
			values = linelist[1:]
			for j in range(10):
				for i in range(10):
					index = i + j * 10
					province = provinces[j]
					year = years[i]
					industry = map_industry[curInd]
					data[year][province][industry] = values[index]

#print(data)


# data format for wage rate will be like:
# {'2008': {
# 	'AB':{
# 		'Goods Producing':33.04,
# 		'Construction':28.63,
# 	},
# 	'BC':{
# 		'Goods Producing':33.04,
# 		'Construction':28.63,
# 	}
# },
# '2009':{
#	'AB':{
# 		'Goods Producing':33.04,
# 		'Construction':28.63,
# 	},
# 	'BC':{
# 		'Goods Producing':33.04,
# 		'Construction':28.63,
# 	}
#}}