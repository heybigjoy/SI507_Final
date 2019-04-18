import csv
import sqlite3
import json

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
                csvWriter.writerow(cleanup(i))


# sqlite_file = 'moma_data.sqlite'
#
# conn = sqlite3.connect(sqlite_file)
# c = conn.cursor()
#
# c.execute('''CREATE TABLE Exhibitions (Id INTEGER PRIMARY KEY AUTOINCREMENT, ExhibitonTitle VARCHAR, ExhibitonBeginDate VARCHAR, ExhibitonEndDate VARCHAR, ExhibitionURL VARCHAR, FOREIGN KEY (Artists_Id) REFERENCES Artists(Id))''')
#
# c.execute('''CREATE TABLE Artists (Id INTEGER PRIMARY KEY AUTOINCREMENT, Nationality VARCHAR, BeginYear INTEGER, EndYear INTEGER, Gender VARCHAR, FOREIGN KEY (Exhibitions_Id) REFERENCES Exhibitions(Id))''')
#
# # json_file = open('countries.json')
# # countries_info = json.loads(json_file.read())
# # json_file.close()
# #
# # countries_info_list = []
# # for country in countries_info:
# #     countries_info_list.append((country['alpha3Code'], country['name'], country['region'], country['population'], country['area']))
#
# with open("MoMAExhibitions1929to1989_clean.csv, r") as inputfile:
#     csvReader = csv.reader(inputfile)
#     header = csvReader.__next__()
#     exhibition_info_list = []
#     for row in csvReader:
#         exhibition_info_list.append((row[0], row[1], row[2], row[3]))
#
# c.executemany('''INSERT into Exhibitions (ExhibitionTitle, ExhibitonBeginDate, ExhibitionEndDate, ExhibitonsURL) VALUES (?,?,?,?)''', exhibitons_info_list)
#
#
# conn.commit()
#
# conn.close()
