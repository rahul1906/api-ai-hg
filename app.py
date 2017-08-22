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
      if req['result']['parameters']['loc_city'] == "" and req['result']['parameters']['loc_code'] == "" and req['result']['parameters']['loc_state'] == "" and req['result']['parameters']['loc_address'] == "":
        return {"messages" : [ {"type" : 0, "speech" : "please enter your location, try entering cities, zipcodes or countries"}]}

      else :
        if  req['result']['parameters']['loc_address'] != "":
          where = req['result']['parameters']['loc_address']
        elif req['result']['parameters']['loc_code'] != "":
          where = req['result']['parameters']['loc_code']
        elif req['result']['parameters']['loc_city'] != "":
          where = req['result']['parameters']['loc_city']
        else : #req['result']['parameters']['loc_state'] != ""
          where = req['result']['parameters']['loc_state']
        
        what = req['result']['parameters']['specialist']
        # where = req['result']['parameters']['geo-city']
        baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&where="+where+"&sortBy=BestMatch"
        #baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&pt="+str(points[0])+"%2C%20"+str(points[1])+"&sortBy=BestMatch"
        data = get_data(baseurl)
        if data[0] == 0:
          # l = []
          # for i in range(0, len(data[1])):
          #   l.append({
          #        "content_type": "text",
          #        "title": data[1][i],
          #        "payload": data[1][i]
          #     })
          return { "messages": [{'title' : "your search matched multiple locations, please select one", "type" : 2, "replies" : data[1]}]}
          # return { "type":2 , "replies": data[1]}  
          # return {"facebook" :{"text": "These are the multiple results that matched your search, please select one","quick_replies": l}}

        elif data[0] == 1:
          # print(data[1])
          res = json.loads(data[1])
          res = create_messages(res)
          return res

        elif data[0] == 2:
          return data[1]

# 'messages': 
#               [
#                {'title': 'when',
#                 'replies': ['12:00',
#                             '13:00',
#                             '17:00',
#                             '18:00'],
#                 'type': 2}],

      
      # data = create_namelist(data)
      # res = create_messages(data)
      
# "quick_replies":[
#       {
#         "content_type":"text",
#         "title":"Red",
#         "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
#       }
#     ]

def create_messages(js):
  
  if len(js['Results']) == 0:
    a = {"messages": [        
    {
                "type": 0,
                "speech": "sorry your search didn't match any results :("
                }
    ]}
    return a

  elif len(js['Results']) >= 5:
    l1 = [{'type':0, 'speech':'These are the results that matched your search'}]
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

  elif len(js['Results']) < 5: 
    l1 = [{'type':0, 'speech':'These are the results that matched your search'}]
    for i in range(0,len(js['Results'])):
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

  else :
    a = {"messages": [        
    {
                "type": 0,
                "speech": "sorry your search didn't match any results :("
                }
    ]}
    return a


def get_data(baseurl):
  headers = {
    "Accept": "application/json",
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSIsImtpZCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSJ9.eyJpc3MiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQiLCJhdWQiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQvcmVzb3VyY2VzIiwiZXhwIjoxNTAzMzgyNTUxLCJuYmYiOjE1MDMzNzg5NTEsImNsaWVudF9pZCI6InBiaC1kZXZlbG9wZXJwb3J0YWwtc3dhZ2dlcmhhcm5lc3MtaW1wbGljaXQtY2xpZW50Iiwic2NvcGUiOiJwYmgucHJvdmlkZXJzZWFyY2gudjRfMCIsInN1YiI6IjgzYmVhOTQ1LWZmZGUtNGYzZC04YzU0LWUwZTBjYWJmNjZjMCIsImF1dGhfdGltZSI6MTUwMjY5MDE1OCwiaWRwIjoiaWRzcnYiLCJQcm92aWRlclNlYXJjaF92NF8wIjoiUGJoX1NlYXJjaF9HZXQiLCJhbXIiOlsicGFzc3dvcmQiXX0.AqO-onSjP6MYQfUt3zVolrIuXVLBQ8_Ajb4iA-hBXEkwAvbs2HGNvwBo8y4yCAqRrCvOUxrxYH9Lkk2qmnAnbe6PyX9-PBmPy_RdHCHtV-PkbvYroPof0mHgmKth1_xneRCf-q_uryWEKSQYo4czDAPTu1mEP450HYIbADy3f5pD4kMKJz3TAI1_IxVxY1liSKLfoGwzxtZbWoTKeSSh2hdH8CJiNMnAbtbI4SM3Ii7wG5EQL_5Agr45HBALbM-PCv6oe-jN3YXTvetlchAeHSuO3AUbF4ASGeP_31_ThmWUUtEHTaxmdV2shv4Asrr5sOFYsb32cHgKIQwWzaV4XA'
  }
  response = requests.get(baseurl, headers=headers)

  if response.status_code == 400:
    js = json.loads(response.text , strict = False)
    if js['Message'].find('matched multiple locations') != -1 :
      return (0, js['Message'].split(':', 1)[-1].split(';'))
    else:
      return (2, {"messages": [        
      {
                  "type": 0,
                  "speech": "sorry your search didn't match any results :("
                  }
      ]})  


  else :  
    text = response.text
    return (1, text)

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