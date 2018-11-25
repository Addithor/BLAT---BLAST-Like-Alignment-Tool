
"""
Fall sem les inn FASTA gögn. Hér lesum við
inn transcript.fasta og skilum lista af query-um.


Output: output_queries.txt

"""

def readFASTA(filename):
	queries = []

	with open(filename) as q:
		while True:
			q.readline()
			query = q.readline().rstrip()
			if len(query) == 0:
				break
			queries.append(query)
	return queries

queries = readFASTA("transcripts.fasta")

"""
2 print skipanir sem prenta út á skjá. Fyrri prentar bara fyrstu 2 query-in
þessi seinni prentar öll query-in í sér línu.
"""
#print(queries[:2])
#print('\n'. join(queries))

# Prentar út og vistar query-in í skrá sem heitir output_queries
with open('output_queries.txt', 'w') as output_data:
	output_data.write('\n'. join(queries))

