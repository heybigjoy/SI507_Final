from SI507project_tools import *
import unittest
import csv
import sqlite3

sqlite_file = 'moma_data.sqlite'

class PartOne(unittest.TestCase):
    def test_moma_clean(self):
        self.cleaned_file = open('MoMAExhibitions1929to1989_clean.csv','r')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Title / first value in the row at index 1")
        self.assertTrue(self.row_reader[100].split(",")[0], "Testing that there is a Title / first value in the row at index 100")
        self.cleaned_file.close()

    def test_moma_clean2(self):
        cleaned_file = open('MoMAExhibitions1929to1989_clean.csv','r')
        self.contents = cleaned_file.readlines()
        cleaned_file.close()
        self.assertTrue("46 Painters and Sculptors under 35 Years of Age,1930,moma.org/calendar/exhibitions/2025,Elsie Driggs,NA,NA,NA,NA,moma.org/artists/49744\n" in self.contents, "Testing that the 46 Painters and Sculptors under 35 Years of Age line exists correctly with proper NAs in the clean file")
        self.assertTrue("Painting in Paris,1930,moma.org/calendar/exhibitions/2024,Maurice Dufrèsne,NA,NA,NA,NA,moma.org/artists/61686\n" in self.contents, "Testing that the Painting in Paris line exists correctly with proper NAs in the clean file")

class PartTwo(unittest.TestCase):
    def test_gender_count(self):
        self.assertEqual(count_gender("1929", "male"), 22, "Testing that gender count has the correct value.")
        self.assertEqual(count_gender("1939", "female"), 8, "Testing that gender count has the correct value.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
