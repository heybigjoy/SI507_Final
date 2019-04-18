import requests, json, csv
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache


START_URL = "https://www.moma.org/calendar/exhibitions/history?locale=zh&utf8=%E2%9C%93&q=&sort_date=opening_date&constituent_id=&mde_type=Exhibition&begin_date=2010&end_date=2019&location=both"
FILENAME = "final_cache.json"

# So I can use 1 (one) instance of the Cache tool -- just one for my whole program, even though I'll get data from multiple places
PROGRAM_CACHE = Cache(FILENAME)

# assuming constants exist as such
# use a tool to build functionality here
def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data) # default here with the Cache.set tool is that it will expire in 7 days, which is probs fine, but something to explore
    return data

#######

main_page = access_page_data(START_URL)

# explore... find that there's a <ul> with class 'topics' and I want the links at each list item...

# I've cached this so I can do work on it a bunch
main_soup = BeautifulSoup(main_page, features="html.parser")
list_of_exhibitions= main_soup.find_all('a',{'class':'calendar-tile__link flex-column'})
#print(list_of_exhibitions) # cool

# for each list item in the unordered list, I want to capture -- and CACHE so I only get it 1 time this week --
# the data at each URL in the list...
#all_states_links = list_of_states.find_all('a')
#print(all_links) # cool

# # Debugging/thinking code:

# for link in list_of_exhibitions:
#     print(link['href'])

# get data of list of parts from the link of each state
exhibition_pages = [] # gotta get all the data in BeautifulSoup objects to work with...
for l in list_of_exhibitions:
    page_data = access_page_data("https://www.moma.org"+l['href'])
    # print(page_data)
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    #print(soup_of_page)
    exhibition_pages.append(soup_of_page)

# list_of_artist = []
# for e in exhibition_pages:
#     try:
#         list_of_artist = e.find_all('li',{'class':'grid-item--artist-term'})
#     except:
#         pass
#     artist_links = list_of_artist.find_all('a')
#     for link in artist_links:
#         print(link['href'])

e1_URL = "https://www.moma.org/calendar/exhibitions/2027?locale=zh"
e1_page = access_page_data(e1_URL)
e1_soup = BeautifulSoup(e1_page, features="html.parser")

list_of_artists = e1_soup.find_all('li',{'class':'grid-item--artist-term'})
artist_links = list_of_artists.find('a')
print(artist_links)



# all_parks_info = []
# all_parks_name = {}
# for state in states_pages:
#     list_of_parks = []
#     list_of_parks = state.find_all('div',{'class':'list_left'})
#     for park in list_of_parks:
#         park_info = []
#         park_soups = []
#         park_name = park.find('h3').text
#         park_link = park.find('a')
#         #print(park_link['href'])
#         park_data = access_page_data("https://www.nps.gov"+park_link['href']+"index.htm")
#         soup_of_park = BeautifulSoup(park_data, features="html.parser")
#         park_states = soup_of_park.find('span',{'class':'Hero-location'}).text
#         print(park_states)
#         if park_states in list(us_state_abbrev.keys()):
#             print(us_state_abbrev[park_states])
#             park_states_abbrev = us_state_abbrev[park_states]
#         else:
#             park_states_abbrev = park_states
#         if park_name not in list(all_parks_name.keys()):
#             all_parks_name[park_name] = ''
#             park_info.append(park_name) #name
#             park_info.append(park.find('h2').text) #type
#             park_info.append(park.find('h4').text) #location
#             park_info.append(park_states_abbrev) #states
#             park_info.append(park.find('p').text) #description
#             all_parks_info.append(park_info)
