'''
You just need to copy the Actual Data link given to you, since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input("Enter Url - ")
uh = urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count =0
sum=0
for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print ("Count : ",count)
print ("Sum : ",sum)
