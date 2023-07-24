"""  Created on Wed Jul 19 2023 """

# Objective : GET issues details / Complete

import requests 
from requests.auth import HTTPBasicAuth
import json

url = "https://auddagiri.atlassian.net/rest/api/3/issue"

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json"
    }

query = {
    'jql':'projects = TJPLE'
    }

response = requests.request(
    'GET',
    url,
    headers=headers,
    params=query,
    auth=("auddagiri@loyaltymethods.com","ATATT3xFfGF04Y9fwg4AO4gH-BocNbwp7CYy-hIEZj5kDTbAf8zpPhKI05M2l7BjVesbkOkS1khtjdk0EHYANihECKEMReuGEGeMIhgmWe-52iOdu48BWig5guDT7k8fXbnPfMBtWTc2fUfKKTpJ8TOO2Y9mSCf6iLQjWT5S38g8u2ctdND7yz0=6FDE7C09")
    )

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",",": ")))

# Objective : GET issue type scheme 

import requests 
from requests.auth import HTTPBasicAuth
import json

url = "https://auddagiri.atlassian.net//rest/api/3/issuetypescheme"

#authentication = HTTPBasicAuth("auddagiri@loyaltymethods.com","<ATATT3xFfGF0BN_wDNxqtO3yAAn8KBGY_4sdJMDfCqK6ldHjUdQS0wf0lpH86hEHk65hBXPyTc27yvRNC54HeLvf5CFacvzQ1QkyDbhM9okZUnQRzU9gQm5wJ41sejkly8FZHajio3KmN0D1noZYetMxzGKJlLOvOWUWkivzXZ_BDhknz7vUCcQ=C4219214>")

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json"
    }

query = {
    'jql':'projects = TJPLE'
    }

response = requests.request(
    'GET',
    url,
    headers=headers,
    params=query,
    auth=("auddagiri@loyaltymethods.com","ATATT3xFfGF04Y9fwg4AO4gH-BocNbwp7CYy-hIEZj5kDTbAf8zpPhKI05M2l7BjVesbkOkS1khtjdk0EHYANihECKEMReuGEGeMIhgmWe-52iOdu48BWig5guDT7k8fXbnPfMBtWTc2fUfKKTpJ8TOO2Y9mSCf6iLQjWT5S38g8u2ctdND7yz0=6FDE7C09")
    )

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",",": ")))

# Objective : POST issue type scheme # not working
import requests 
from requests.auth import HTTPBasicAuth
import json

url = "https://auddagiri.atlassian.net/rest/api/3/issue/issuetypescheme"

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json"
    }

payload = json.dumps({
     "defaultIssueTypeId":"10002",
     "description":'Post issue type schema',
     "issueTypeIds":[
         "10001",
         "10002",
         "10003"],
     "name":"Did this update run through to jira"
     })

response = requests.request(
    'POST',
    url,
    data=payload,
    headers=headers,
    auth=("auddagiri@loyaltymethods.com","ATATT3xFfGF04Y9fwg4AO4gH-BocNbwp7CYy-hIEZj5kDTbAf8zpPhKI05M2l7BjVesbkOkS1khtjdk0EHYANihECKEMReuGEGeMIhgmWe-52iOdu48BWig5guDT7k8fXbnPfMBtWTc2fUfKKTpJ8TOO2Y9mSCf6iLQjWT5S38g8u2ctdND7yz0=6FDE7C09")
    )

response.raise_for_status()

#print(response.text)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",",": ")))


# Objective : POST new issues in Jira from python / not working (tried for 3 hours)
import requests 
from requests.auth import HTTPBasicAuth
import json

url = "https://auddagiri.atlassian.net/rest/api/3/issue/issuetype"

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json"
    }

payload = json.dumps({
     "fields":{
         "project":{
                 "key":"TJPLE"
                 },
                 "summary":"Did this update run through to jira",
                 "description":"creating a issue using project key and issue name",
                 "issuetype": {
                             "name":"Task"
                             }}})

response = requests.request(
    'POST',
    url,
    data=payload,
    headers=headers,
    auth=("auddagiri@loyaltymethods.com","ATATT3xFfGF04Y9fwg4AO4gH-BocNbwp7CYy-hIEZj5kDTbAf8zpPhKI05M2l7BjVesbkOkS1khtjdk0EHYANihECKEMReuGEGeMIhgmWe-52iOdu48BWig5guDT7k8fXbnPfMBtWTc2fUfKKTpJ8TOO2Y9mSCf6iLQjWT5S38g8u2ctdND7yz0=6FDE7C09")
    )

#print(response.text)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",",": ")))

# Objective :Get issues 

import requests 
from requests.auth import HTTPBasicAuth
import json

server = "https://auddagiri.atlassian.net/rest/api/3/issue"

authentication = HTTPBasicAuth("auddagiri@loyaltymethods.com","<ATATT3xFfGF0HOhJcxeiBSOjtG9jhqfmyCNKkZsoN1Dojqx7F9-7GD9W1H_5w8BkQ1-SQszWnLBu6DMf4qBra-a89Uww3jkUJU8PJeSAHKGGjg8Zq-pv-0zGHtE2VKcfYGfv3OriqM2sj7ixwoLTuDhYQvKGI3FTx6i1uhPkta9E6vo5hEtbPSc=0ATATT3xFfGF0HOhJcxeiBSOjtG9jhqfmyCNKkZsoN1Dojqx7F9-7GD9W1H_5w8BkQ1-SQszWnLBu6DMf4qBra-a89Uww3jkUJU8PJeSAHKGGjg8Zq-pv-0zGHtE2VKcfYGfv3OriqM2sj7ixwoLTuDhYQvKGI3FTx6i1uhPkta9E6vo5hEtbPSc=0FA2A535FA2A535>")

headers = {
    "Accept":"application/json"
    }

response = requests.request(
    'GET',
    server,
    headers=headers,
    auth=authentication
    )

try:
    if response.text.strip(): 
        data = response.json()
        print(json.dumps(data,sort_keys=True, indent=4, separators=(',',':')))
    else:
        print('Error: empty json')
except json.JSONDecodeError as e:
    print('Error decoding json:',e)


# Copy Objective :Get issues 

import requests 
from requests.auth import HTTPBasicAuth
import json

server = "https://auddagiri.atlassian.net/rest/api/3/search"

authentication = HTTPBasicAuth("auddagiri@loyaltymethods.com","<ATATT3xFfGF0HOhJcxeiBSOjtG9jhqfmyCNKkZsoN1Dojqx7F9-7GD9W1H_5w8BkQ1-SQszWnLBu6DMf4qBra-a89Uww3jkUJU8PJeSAHKGGjg8Zq-pv-0zGHtE2VKcfYGfv3OriqM2sj7ixwoLTuDhYQvKGI3FTx6i1uhPkta9E6vo5hEtbPSc=0ATATT3xFfGF0HOhJcxeiBSOjtG9jhqfmyCNKkZsoN1Dojqx7F9-7GD9W1H_5w8BkQ1-SQszWnLBu6DMf4qBra-a89Uww3jkUJU8PJeSAHKGGjg8Zq-pv-0zGHtE2VKcfYGfv3OriqM2sj7ixwoLTuDhYQvKGI3FTx6i1uhPkta9E6vo5hEtbPSc=0FA2A535FA2A535>")

headers = {
    "Accept":"application/json"
    }

response = requests.request(
    'GET',
    server,
    headers=headers,
    auth=authentication
    )

try:
    if response.text.strip(): 
        data = response.json()
        print(json.dumps(data,sort_keys=True, indent=4, separators=(',',':')))
    else:
        print('Error: empty json')
except json.JSONDecodeError as e:
    print('Error decoding json:',e)

response.raise_for_status()

print(json.loads(response.text))


print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",",": ")))




# Other codes types 

# Objective : API token for rest calls 

from jira import JIRA
# authenticate
user_name = ''
token = 'ATATT3xFfGF0HOhJcxeiBSOjtG9jhqfmyCNKkZsoN1Dojqx7F9-7GD9W1H_5w8BkQ1-SQszWnLBu6DMf4qBra-a89Uww3jkUJU8PJeSAHKGGjg8Zq-pv-0zGHtE2VKcfYGfv3OriqM2sj7ixwoLTuDhYQvKGI3FTx6i1uhPkta9E6vo5hEtbPSc=0ATATT3xFfGF0HOhJcxeiBSOjtG9jhqfmyCNKkZsoN1Dojqx7F9-7GD9W1H_5w8BkQ1-SQszWnLBu6DMf4qBra-a89Uww3jkUJU8PJeSAHKGGjg8Zq-pv-0zGHtE2VKcfYGfv3OriqM2sj7ixwoLTuDhYQvKGI3FTx6i1uhPkta9E6vo5hEtbPSc=0FA2A535FA2A535'
# access

server = 'https://auddagiri.atlassian.net/rest/api/2/search?jql=project%3D${projectName}%20AND%20(status%3DDONE)'

options = {
    'server':server
    }
#define
jira = JIRA(options,basic_auth=(user,apikey)) # jira.JIRA
#extract
ticket = 'KRP-11697'
issue = jira.issue(ticket)

summary = issue.fields.summary 

print('ticket:',ticket,summary)

# for multiple 

for project in jira.projects():
    print(project.key)






# Objective - using jira lbrary for python integration 
from jira import JIRA

# construct a client instance 
jira_web = {'server':"https://_____python.atlassian.net"}

# pass authentication paramters 

jira = JIRA(options=jiraOptions,basic_auth=("auddagiri@loyaltymethods.com",
                                            "Tap2Shazam!"))

# call the multiple instances 

for singleIssue in jira.search_issues(jql_str='project = med_bugs'):
    print('{}:{}:{}'.format(singleIssue.key,
    singleIssue.fields,summary,singleIssue.fields.reporter.displayName))

# to call a single instance
singleIssue = jira.issue('MED-1')
print('{}:{}:{}'.format(singleIssue.key,
                        singleIssue.fields.summary,
                        singleIssue.fields.reporter.displayName)) 

# jira rest API for jira python integration

import requests 
from requests.auth import HTTPBasicAuth
import json 
import pandas as pd 

url = "https://         python.atlassian.net/rest/api/2/search"

# create authentication object
auth = TPBasicAuth("auddagiri@loyaltymethods.com",
                                            "Tap2Shazam!") 

headers = {"Accept":"application/json"}

query = {'jql':'project:MedicineAppBugs'}

# generate a request object 

response = requets.request("GET",url,headers=headers,auth=auth,params=query)

projectIssues = json.dumps(json.loads(response.text),
                           sort_keys=True,indent=6,separators=(",",":"))

# convert nested object to dict 

dictProjectIssues = json.loads(projectIssues)
listALLIssues = []
keyIssue , keySummary, keyReporter = "","",""

# acess the issues from project 

def 

