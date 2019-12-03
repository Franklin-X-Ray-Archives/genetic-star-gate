from Bio import Entrez
Entrez.email = "jm@ciencias.com"  # Always tell NCBI who you are
handle = Entrez.egquery(term="Opuntia AND rpl16")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"]=="nuccore":
        print(row["Count"])

handle = Entrez.esearch(db="nuccore", term="Opuntia AND rpl16")
record = Entrez.read(handle)
gi_list = record["IdList"]
gi_list
gi_str = ",".join(gi_list)
handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb", retmode="text")
text = handle.read()
print(text)
