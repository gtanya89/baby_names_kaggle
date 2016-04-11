def most_popular_names():

	file=open("NationalNames.csv")
	data=[]
	list_data=file.read().split()
	for i in range(1,len(list_data)):
		data.append(list_data[i].split(","))
	#print data

	names_1938_1950=[]
	names_1951_1963=[]

	for record in data:
		if record[3]=='M' and int(record[2])>= 1938 and int(record[2])<=1950:
			names_1938_1950.append([record[1], int(record[4])])
		if record[3]=='M' and int(record[2])>= 1951 and int(record[2])<=1963:
			names_1951_1963.append([record[1], int(record[4])])

	names_1938_1950=sorted(names_1938_1950, key=lambda x:(-x[1],x[0]))
	names_1951_1963=sorted(names_1951_1963, key=lambda x:(-x[1],x[0]))

	counter=0
	i=0
	most_popular_names_1938_1950=[]
	while counter<10:
		record=names_1938_1950[i]
		if record[0] in most_popular_names_1938_1950:
			i+=1
			continue
		else:
			most_popular_names_1938_1950.append(record[0])
			counter+=1
			i+=1
	

	print "Top 10 most popular boy names between 1938 and 1950 are: ", most_popular_names_1938_1950

	counter=0
	i=0
	most_popular_names_1951_1963=[]
	while counter<10:
		record=names_1951_1963[i]
		if record[0] in most_popular_names_1951_1963:
			i+=1
			continue
		else:
			most_popular_names_1951_1963.append(record[0])
			counter+=1
			i+=1
	

	print "Top 10 most popular boy names between 1951 and 1963 are: ", most_popular_names_1951_1963

	names_losing_popularity=list(set(most_popular_names_1938_1950)-set(most_popular_names_1951_1963))

	print "Names that lost popularity: ", names_losing_popularity
	
if __name__=='__main__':
	most_popular_names()
