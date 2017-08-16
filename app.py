#!/usr/bin/env python
from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError


import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

string = r"""
    {
  "id": "92dd2f9c-5756-4066-a98d-3089fbd67845",
  "timestamp": "2017-08-16T11:28:06.126Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "NV",
    "action": "search_doctors",
    "actionIncomplete": false,
    "parameters": {
      "specialist": "Orthopedic",
      "state": "NV"
    },
    "contexts": [],
    "metadata": {
      "intentId": "f54a8cb3-26be-4279-8e2e-6545853f93c3",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "intentName": "search-doctors"
    },
    "fulfillment": {
      "speech": "these are the doctors that matched your search...",
      "messages": [
        {
          "type": 0,
          "speech": "these are the doctors that matched your search..."
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 206,
    "errorType": "partial_content",
    "errorDetails": "Webhook call failed. Error: Request timeout."
  },
  "sessionId": "07c1d1ca-af0b-4fb7-8531-bfabc1b2ec4f"
}

    """

@app.route('/chat', methods=['GET'])
def web():    
    return "WELCOME :)"


@app.route('/webhook', methods=['POST'])
def webhook():
    
    req = request.get_json(silent=True, force=True)
    #req = json.loads(req, strict=False)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get("result").get("action") != "search_doctors":
        return {}
    else :
      what = req['result']['parameters']['specialist']
      where = req['result']['parameters']['state']
      baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&where="+where+"&sortBy=Score"
      data = get_data(baseurl)
      data = json.loads(data)
      data = create_namelist(data)
      res = create_messages(data)
      return res


def get_data(baseurl):
  headers = {
    "Accept": "application/json",
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSIsImtpZCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSJ9.eyJpc3MiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQiLCJhdWQiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQvcmVzb3VyY2VzIiwiZXhwIjoxNTAyODg1MDUwLCJuYmYiOjE1MDI4ODE0NTAsImNsaWVudF9pZCI6InBiaC1kZXZlbG9wZXJwb3J0YWwtc3dhZ2dlcmhhcm5lc3MtaW1wbGljaXQtY2xpZW50Iiwic2NvcGUiOiJwYmgucHJvdmlkZXJzZWFyY2gudjRfMCIsInN1YiI6IjgzYmVhOTQ1LWZmZGUtNGYzZC04YzU0LWUwZTBjYWJmNjZjMCIsImF1dGhfdGltZSI6MTUwMjY5MDE1OCwiaWRwIjoiaWRzcnYiLCJQcm92aWRlclNlYXJjaF92NF8wIjoiUGJoX1NlYXJjaF9HZXQiLCJhbXIiOlsicGFzc3dvcmQiXX0.Rii_eol11i3hPV0juon31EJbZgjUob6gCrV0lnJkPFfEbA9DyweNxwSM33Avz40AJHDRb-aydtZoPhVQ_G8mdcJqjjr33OSZ2uzS-y7WgWWNjAUVtOTrK8cSPv3LTyxKRpSSQxOLjfNc_ekqMeFOVDPArET-0BnNxfFBz3lY206ZtLSz3XH0jvfwxwVoKkusuaLvsashjZ6-HMwYLoBFWFVqJ0duZCJAaRnssmAU_zy7y38orrWVCcaux0Hk0RexseB6brOl-Dbv1NzSLnOwKVteThDbzgjY305ZczUuCZysFFh6JeDeCh9B2Sb5ibjrZ5RudBtHSYn8v-Z_6CF92Q'
  }
  response = requests.get(baseurl, headers=headers)
  text = response.text
  return text

def create_namelist(data):
    l = []
    for i in range(0, 5):
        l.append(data['Results'][i]['DemographicInfo']['DisplayName'])
    return l  

def create_messages(l):
    l1 = [{'type':0,'speech':'these are the top 5 results that matched your search...'}]
    for i in l:
        a = {"type":0,
        "speech":i}
        l1.append(a)
    return {"messages":l1}

# def processRequest(req):
#     names = create_namelist(req)
#     return create_messages(names)


# def create_namelist(data):
#     l = []
#     for i in range(0, 5):
#         l.append(data['Results'][i]['DemographicInfo']['DisplayName'])
#     return l


# def create_messages(l):
#     l1 = [{'type':0,'speech':'these are the top 5 results that matched your search...'}]
#     for i in l:
#         a = {"type":0,
#         "speech":i}
#         l1.append(a)
#     return {"messages":l1}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')