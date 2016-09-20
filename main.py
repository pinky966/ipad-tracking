import requests
# 1: use the key as a variable
# key = B3jiljfdlk
# url = first part + key + second part
# 2: use dates as variables (in the same way) - DON'T let them be strings, let them be dates
# 3: create the url as a function where you give it the key and 2 dates
url = 'https://www.rescuetime.com/anapi/data?key=B63T_60UzyUHWKqKjiQ31a3hWs6Sp__RtzfqYya3&operation=select&perspective=rank&restrict_kind=activity&restrict_begin=2016-08-07&restrict_end=2016-09-20&format=json'
response = requests.get(url)
print (response.json())

import json
dict = response.json()

# 4: Print out ALL categories that are in the dictionary (categories in index 4)
# 5: Print out ALL categories WITH the time spent aggregated (index 2 of each row is time in seconds)

# 6: Above and Beyond: give an OPTION: print all sites with time spent aggregated
# 7: make it alphabetical by site name (sort index 3 of each row alphabetically)
# 8: give another option that will list most time spent first (sort index 2 of each row, great to least)

print("end")

#