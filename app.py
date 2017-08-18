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


@app.route('/chat', methods=['GET'])
def web():    
    return "WELCOME :)"


@app.route('/webhook', methods=['POST'])
def webhook():
    
    req = request.get_json(silent=True, force=True)
    #req = json.loads(string , strict=False)

    #print("Request:")
    #print(json.dumps(req, indent=4))
    # print(type(req))

    res = processRequest(req)
    # print(type(res))
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
      where = req['result']['parameters']['geo-city']
      baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&where="+where+"&sortBy=BestMatch"
      #baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&pt="+str(37.479189)+"%2C%20"+str(-122.165982)+"&sortBy=BestMatch"
      data = get_data(baseurl)
      data = json.loads(data)
      # data = create_namelist(data)
      # res = create_messages(data)
      res = create_messages(data)
      return res

def create_messages(js):

  if len(js['Results']) >= 5:
    l1 = []
    for i in range(0, 5):
      a = {
      "type" : 1,
      "title" : js['Results'][i]['DemographicInfo']['DisplayName'],
      "subtitle" : js['Results'][i]['DemographicInfo']['DisplayLastName'],
      "imageUrl" : js['Results'][i]['DemographicInfo']['ImagePaths'][2]['Url'],
      "buttons" : [{
        "text" : "visit page" ,
        "postback" : js['Results'][i]['DemographicInfo']['ProviderUrl']
      }]
      }
      l1.append(a)
      
    print({"messages" : l1})
    return {"messages" : l1}

  else :  
    for i in range(0,len(js['Results'])):
      l1 = []
      # l1 = [{'type':0,'speech':'these are the results that matched your search...'}]
      # print(js['Results'][i]['DemographicInfo']['DisplayName'])
      # print(js['Results'][i]['DemographicInfo']['ProviderUrl'])
      # print(js['Results'][i]['DemographicInfo']['ImagePaths'][0]['Url'])
      # print(js['Results'][i]['DemographicInfo']['DisplayLastName'])
      a = {
      "type" : 1,
      "title" : js['Results'][i]['DemographicInfo']['DisplayName'],
      "subtitle" : js['Results'][i]['DemographicInfo']['DisplayLastName'],
      "imageUrl" : js['Results'][i]['DemographicInfo']['ImagePaths'][2]['Url'],
      "buttons" : [{
        "text" : "visit page" ,
        "postback" : js['Results'][i]['DemographicInfo']['ProviderUrl']
      }]
      }
      l1.append(a)
      
    print({"messages" : l1})  
    return {"messages" : l1}

def get_data(baseurl):
  headers = {
    "Accept": "application/json",
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSIsImtpZCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSJ9.eyJpc3MiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQiLCJhdWQiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQvcmVzb3VyY2VzIiwiZXhwIjoxNTAzMDU1ODkyLCJuYmYiOjE1MDMwNTIyOTIsImNsaWVudF9pZCI6InBiaC1kZXZlbG9wZXJwb3J0YWwtc3dhZ2dlcmhhcm5lc3MtaW1wbGljaXQtY2xpZW50Iiwic2NvcGUiOiJwYmgucHJvdmlkZXJzZWFyY2gudjRfMCIsInN1YiI6IjgzYmVhOTQ1LWZmZGUtNGYzZC04YzU0LWUwZTBjYWJmNjZjMCIsImF1dGhfdGltZSI6MTUwMjY5MDE1OCwiaWRwIjoiaWRzcnYiLCJQcm92aWRlclNlYXJjaF92NF8wIjoiUGJoX1NlYXJjaF9HZXQiLCJhbXIiOlsicGFzc3dvcmQiXX0.ZL2lVdoPiWTQCqXmEp440JmXvIBmlLql30TtmeecS7vVEizt9U-IPyqoKoExaiwuwnn_6q_Xer9E4wc8kN5PXBqD1cUVQtaO_u4Fl3PE4I52dAQyQK9jc8BZmttJ2KVYbYDJ0dLX_zvVGoqiGzZx1lDQMX-3hngl_a-rpTmlDxTq5bW683RnUjMAudEJan-PnABCiiXNPubUeZFg1Z8eoz8HYk5WLauxXcKaawTWeey_JNg0GRsG99WLeTbb9qJWBQ9XjA9qvGFa2cRgBbS3tRINU6kgXw5GyXXD6qrx5lTvVMQu1Ffa4zdFm75ez5nDEwTKYV28uTS0hq_w5aIwAg'
  }
  response = requests.get(baseurl, headers=headers)
  text = response.text
  return text

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