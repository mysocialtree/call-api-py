import urllib.request
import json
# url https://mstree.de/api/get.php + ? + api=token
page = urllib.request.urlopen('https://mstree.de/api/get.php?api=token')
# read data
load =  page.read()
# convert data to json
json = json.loads(load)
#print data id
print(json["id"])
