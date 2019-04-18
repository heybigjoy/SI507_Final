import csv
from advanced_expiry_caching import Cache

def cleanup(row):
    newRow = []
    newRow.extend([row[2], row[4], row[5], row[7], row[12], row[19], row[20], row[21], row[23], row[27]])
    for n in range(len(newRow)):
        if newRow[n] == "":
            newRow[n] = "N/A"
    return newRow

with open("MoMAExhibitions1929to1989.csv", "r", encoding="ISO-8859-1") as inputfile:
    csvReader = csv.reader(inputfile)
    with open("MoMAExhibitions1929to1989_clean.csv", "w") as outputfile:
        header = csvReader.__next__()
        csvWriter = csv.writer(outputfile)
        csvWriter.writerow(cleanup(header))
        for i in csvReader:
            if (i[8] == "Artist" and i[11] == "Individual"):
                print(cleanup(i))
                csvWriter.writerow(cleanup(i))
