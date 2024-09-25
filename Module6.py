'''
You just need to copy the Actual Data link given to you, since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

#########    The code for the second assignment is below this code    #################
######################n      This is for the first assignment      ####################
import json
from urllib.request import urlopen

count = 0
sum = 0
url = input("Enter Url - ")

# Fetch the data from the URL
data = urlopen(url).read()

# Decode the data from bytes to a string
info = json.loads(data.decode('utf-8'))

# Loop through the comments and calculate the sum and count
for i in info['comments']:
    count += 1
    sum += i['count']

# Print the results
print("Sum:", sum)
print("Count:", count)


##########################    Code for second assignment: Using a Geo Location API    ########################

from urllib.request import urlopen
import json
import urllib.parse

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:
    address = input("Enter location: ")

    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})

    uh = urlopen(url)
    data = uh.read().decode('utf-8')
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        continue

    placeid = js["results"][0]['place_id']
    print("Place id", placeid)
