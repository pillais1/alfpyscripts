
import requests
from requests.auth import HTTPBasicAuth
import csv

getPathURL="http://10.15.16.208:8080/alfresco/service/jabil/getNodePath?nodeRef=workspace://SpacesStore/"

def getPathFromNodeRef(nodeRef):
        r=requests.get(getPathURL+nodeRef,auth=HTTPBasicAuth('username','password'))
        print(r.content)

with open('2016batchWS.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                getPathFromNodeRef(row['uuid'])
