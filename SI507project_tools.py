import csv
import sqlite3
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

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
        if (newRow[n] == "" ):
            newRow[n] = "NA"
        if (newRow[n] == "" ):
            newRow[n] = "NA"
        if (newRow[n] == "Male" ):
            newRow[n] = "male"
        if (newRow[n] == "Female" ):
            newRow[n] = "female"

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
    c.execute('''CREATE TABLE IF NOT EXISTS Artists (ArtistId INTEGER PRIMARY KEY AUTOINCREMENT, ArtistName VARCHAR UNIQUE, Nationality VARCHAR, BeginYear INTEGER, EndYear INTEGER, Gender VARCHAR, ArtistURL VARCHAR)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Exhibitions (ExhibitionId INTEGER PRIMARY KEY AUTOINCREMENT, ExhibitionTitle VARCHAR UNIQUE, ExhibitionYear VARCHAR, ExhibitionURL VARCHAR)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Exhibition_Artist (ExhibitionId INTEGER, ArtistId INTEGER, FOREIGN KEY (ExhibitionId) References Exhibitions(ExhibitionId), FOREIGN KEY (ArtistId) References Artists(ArtistId))''')
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
            c.execute('''SELECT ExhibitionId from Exhibitions where ExhibitionTitle = ?''', (row[0],))
            ExhibitionId = c.fetchone()[0]
            c.execute('''SELECT ArtistId from Artists where ArtistName = ?''', (row[3],))
            ArtistId = c.fetchone()[0]
            exhibitions_artists_info_list.append((ExhibitionId, ArtistId))
    c.executemany('''INSERT into Exhibition_Artist (ExhibitionId, ArtistId) VALUES (?,?)''', exhibitions_artists_info_list)
    conn.commit()
    conn.close()

def count_gender(Year, Gender):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''SELECT COUNT (*)
                FROM Exhibitions, Artists, Exhibition_Artist
                WHERE Exhibition_Artist.ExhibitionId = Exhibitions.ExhibitionId
                AND Exhibition_Artist.ArtistId = Artists.ArtistId
                AND ExhibitionYear = ?
                AND Gender = ? ''', (Year, Gender))
    count = c.fetchall()[0][0]
    conn.close()
    return count

def gender_distribution(FromYear, ToYear):
    male_count = 0
    female_count = 0
    male_count_list = []
    female_count_list = []
    year_list = []

    for year in range(int(FromYear),int(ToYear)+1):
        year_list.append(year)
        male_count += count_gender(year, 'male')
        female_count += count_gender(year, 'female' )
        male_count_list.append(male_count)
        female_count_list.append(female_count)

    trace0 = go.Scatter(
        x = year_list,
        y = male_count_list,
        name = "male"
    )

    trace1 = go.Scatter(
        x = year_list,
        y = female_count_list,
        name = "female"
    )

    data = [trace0, trace1]

    layout = go.Layout(
        title='MoMA Gender Distribution from ' + FromYear + ' to ' + ToYear,
        xaxis=dict(
            title='Year'
        ),
        yaxis=dict(
            title='Gender'
        ),
    )

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
