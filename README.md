# SI507_project4
This projects allows user to scrap and cache data from the national park service website(https://www.nps.gov) and organize the data into a clean-up csv file with all the site name, type, location and desctiption as the output. An example csv file is included as sample_site_dataset.csv. 

## Getting Started
This project imports a BeautifulSoup module. You can install it and everything else you need from requirements.txt
This project also needs to import requests, json, and csv, as well as all the functions from advanced_expiry_caching.py(included in the folder, author: Megh Marathe) to cache the data.

## Other Details
The SI507_project4.py allows you to scrap data from the nps website and organize the data.

## To run this project:
- In the terminal, find the directory of this project.
- Run the code using this command: python3 SI507_project4.py
- The several file will be created after you run the code:
	- "project4_cache.json"
	- "site_dataset.csv"
	- "site_dataset_clean.csv" (This one is the final output file you will be checking on.)
