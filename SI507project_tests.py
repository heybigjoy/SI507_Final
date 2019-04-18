from SI507project_tools import *
import unittest
import csv
#import numpy as np
import random
import itertools

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
        self.assertTrue("46 Painters and Sculptors under 35 Years of Age,4/11/1930,4/27/1930,moma.org/calendar/exhibitions/2025,A. Everett Austin, Jr.,N/A,N/A,N/A,N/A,moma.org/artists/16555\n" in self.contents, "Testing that the 46 Painters and Sculptors under 35 Years of Age line exists correctly with proper NAs in the clean file")
        self.assertTrue("Modern Architecture: International Exhibition,2/9/1932,3/23/1932,moma.org/calendar/exhibitions/2044,Russell G. Cory,N/A,N/A,N/A,N/A,moma.org/artists/63223\n" in self.contents, "Testing that Modern Architecture: International Exhibition is correct in resulting file with proper NAs in the clean file")

#
# class PartTwo(unittest.TestCase):
#     def test_median_rating(self):
#         self.assertEqual(median_rating, "PG-13", "Testing that median_rating has the correct value. NOTE that of course, hard-coding what you see on your screen is not acceptable here, even though we can't AUTOMATICALLY test your coding process -- you should write code to achieve this result; humans will look at submissions.")
#
# class PartThree(unittest.TestCase):
#     def test_sample_fake_movies1(self):
#         self.assertTrue(len(sample_fake_movies.split("\n")) >= 10, "Testing that there are at least 10 lines in sample_fake_movies (note that other constraints will be tested manually by humans to assure full points on this question -- deductions may still occur if instructions were not followed)")
#
#     def test_sample_fake_movies2(self):
#         self.assertTrue( (len(sample_fake_movies.split("\n")[0]) <= 45) or (len(sample_fake_movies.split("\n")[0]).split() <= 9), "Testing that sample fake movies abides by constraints for length or word # in title")
#

if __name__ == "__main__":
    unittest.main(verbosity=2)
