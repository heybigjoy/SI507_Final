import csv
import sqlite3
import json

sqlite_file = 'moma_data.sqlite'
csv_file = 'MoMAExhibitions1929to1989.csv'
cleanup_csv_file = 'MoMAExhibitions1929to1989_clean.csv'

def modify_datetoyear(str):
    str = str[-4:]
    return str

def cleanup_tool(row):
    newRow = []
    newRow.extend([row[2], modify_datetoyear(row[4]), row[7], row[12], row[19], row[20], row[21], row[23], row[27]])
    for n in range(len(newRow)):
        if (newRow[n] == "" and newRow[n] == "NULL"):
            newRow[n] = "NA"
    return newRow

def cleanup():
    with open(csv_file, "r", encoding="ISO-8859-1") as inputfile:
        csvReader = csv.reader(inputfile)
        with open(cleanup_csv_file, "w") as outputfile:
            header = csvReader.__next__()
            csvWriter = csv.writer(outputfile)
            csvWriter.writerow(cleanup_tool(header))
            for i in csvReader:
                if (i[8] == "Artist" and i[11] == "Individual"):
                    csvWriter.writerow(cleanup_tool(i))

def create_table():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Artists (Id INTEGER PRIMARY KEY AUTOINCREMENT, ArtistName VARCHAR UNIQUE, Nationality VARCHAR, BeginYear INTEGER, EndYear INTEGER, Gender VARCHAR, ArtistURL VARCHAR)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Exhibitions (Id INTEGER PRIMARY KEY AUTOINCREMENT, ExhibitionTitle VARCHAR UNIQUE, ExhibitionYear VARCHAR, ExhibitionURL VARCHAR)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Exhibition_Artist (ExhibitionID INTEGER, ArtistId INTEGER, FOREIGN KEY (ExhibitionId) References Exhibitions(Id), FOREIGN KEY (ArtistId) References Artists(Id))''')
    conn.commit()
    conn.close()

def insert_artists():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    with open(cleanup_csv_file, "r") as inputfile:
        csvReader = csv.reader(inputfile)
        header = csvReader.__next__()
        artists_info_list = []
        for row in csvReader:
            artists_info_list.append((row[3], row[4], row[5], row[6], row[7], row[8]))

    c.executemany('''INSERT OR REPLACE into Artists (ArtistName, Nationality, BeginYear, EndYear, Gender, ArtistURL) VALUES (?,?,?,?,?,?)''', artists_info_list)
    conn.commit()
    conn.close()


def insert_exhibitions():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    with open(cleanup_csv_file, "r") as inputfile:
        csvReader = csv.reader(inputfile)
        header = csvReader.__next__()
        exhibitions_info_list = []
        for row in csvReader:
            exhibitions_info_list.append((row[0], row[1], row[2]))

    c.executemany('''INSERT OR REPLACE into Exhibitions (ExhibitionTitle, ExhibitionYear, ExhibitionURL) VALUES (?,?,?)''', exhibitions_info_list)
    conn.commit()
    conn.close()

def insert_exhibitions_artists():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    with open(cleanup_csv_file, "r") as inputfile:
        csvReader = csv.reader(inputfile)
        header = csvReader.__next__()
        exhibitions_artists_info_list = []
        for row in csvReader:
            c.execute('''SELECT Id from Exhibitions where ExhibitionTitle = ?''', (row[0],))
            ExhibitionId = c.fetchone()[0]
            c.execute('''SELECT Id from Artists where ArtistName = ?''', (row[3],))
            ArtistId = c.fetchone()[0]
            exhibitions_artists_info_list.append((ExhibitionId, ArtistId))
    c.executemany('''INSERT into Exhibition_Artist (ExhibitionId, ArtistId) VALUES (?,?)''', exhibitions_artists_info_list)
    conn.commit()
    conn.close()

def Exhibition_Id_List(Year):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''SELECT Id from Exhibitions where ExhibitionYear = ?''', (Year,))
    data = []
    for row in c:
        data.append(str(row[0]))
    conn.close()
    return data

def Gender_Distribution(Year):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    artist_list = []
    gender_list = []
    for e in Exhibition_Id_List(Year):
        c.execute('''SELECT ArtistId from Exhibition_Artist where ExhibitionId = ?''', (e,))
        for row in c:
            artist_list.append(str(row[0]))
    for a in artist_list:
        c.execute('''SELECT Gender from Artists where Id = ?''', (a,))
        for row in c:
            gender_list.append(str(row[0]))
    conn.close()
    male_count = gender_list.count("Male")
    female_count = gender_list.count("Female")
    return {"Male":male_count, "Female": female_count, "Year": Year}

def Year_List():
    year_list = []
    for year in range(1929,1990):
        year_list.append(year)
    return year_list

def Gender_List(gender):
    gender_count_list = []
    for i in Year_List():
        gender_count_list.append(Gender_Distribution(i)[gender])
    return gender_count_list
