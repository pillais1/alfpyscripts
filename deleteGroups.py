#add the username and password while executing the script
import csv
import urllib
import httplib2

with open('groupsToDelete.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	h = httplib2.Http(".cache")
	h.add_credentials('username', 'password')
	headers = {'Content-type':'application/json'}
	for row in reader:
		resp,content = h.request("http://serverip:port/alfresco/service"+row['url'],'DELETE',headers=headers)