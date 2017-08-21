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

    # print()
    # print()

def processRequest(req):
    # print(type(req['result']['actionIncomplete']), type(req['result']['parameters']['geo-city']))
   
    # if req['result']['actionIncomplete'] == True and req['result']['parameters']['geo-city'] == "":
    #   print('inside if')
      
    if req.get('result').get('action') == "show_coordinates":
      points = get_coordinates_fb(req['result']['parameters']['any'])
      return {"messages":[        
      {
                  "type": 0,
                  "speech": "latitiude : "+points[0]+"longitude : "+points[1]+""
                  }
      ] }
 
    if req.get("result").get("action") == "search_doctors":
      
      what = req['result']['parameters']['specialist']
      where = req['result']['parameters']['geo-city']
      points = get_coordinates_google(where)
      #baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&where="+where+"&sortBy=BestMatch"
      baseurl = "https://pbh-uat.healthgrades.com/api/v4_0/providersearch/v4_0/pbh/search?cID=PBHTEST_007&providerType=None&what="+what+"&pt="+str(points[0])+"%2C%20"+str(points[1])+"&sortBy=BestMatch"
      data = get_data(baseurl)
      data = json.loads(data)
      # data = create_namelist(data)
      # res = create_messages(data)
      res = create_messages(data)
      return res
    
    else : 
      return {}

def get_coordinates_fb(res):
  lat = js['entry'][0]['messaging'][0]['message']['attachments'][0]['payload']['coordinates']['lat']
  lon = js['entry'][0]['messaging'][0]['message']['attachments'][0]['payload']['coordinates']['long']
  return (lat, lon)


def get_coordinates_google(city):
  url = "http://maps.googleapis.com/maps/api/geocode/json?address="+city+"&sensor=true"
  text = get_data1(url)
  js = json.loads(text , strict = False)
  print(js)
  lat = js['results'][0]['geometry']['location']['lat']
  lon = js['results'][0]['geometry']['location']['lng']
  print(lat , lon)
  return (lat,lon)


def get_data1(baseurl):
  headers = {
    "Accept": "application/json",
  }
  response = requests.get(baseurl, headers=headers)
  text = response.text
  return text


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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSIsImtpZCI6IjZCdFdLZ1g5RDd1ZGowYTJyLWkyZGFiN3dKRSJ9.eyJpc3MiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQiLCJhdWQiOiJodHRwczovL3BiaC11YXQuaGVhbHRoZ3JhZGVzLmNvbS9hcGkvdjFfMC9zdHMvaWRlbnQvcmVzb3VyY2VzIiwiZXhwIjoxNTAzMzAxNzU4LCJuYmYiOjE1MDMyOTgxNTgsImNsaWVudF9pZCI6InBiaC1kZXZlbG9wZXJwb3J0YWwtc3dhZ2dlcmhhcm5lc3MtaW1wbGljaXQtY2xpZW50Iiwic2NvcGUiOiJwYmgucHJvdmlkZXJzZWFyY2gudjRfMCIsInN1YiI6IjgzYmVhOTQ1LWZmZGUtNGYzZC04YzU0LWUwZTBjYWJmNjZjMCIsImF1dGhfdGltZSI6MTUwMjY5MDE1OCwiaWRwIjoiaWRzcnYiLCJQcm92aWRlclNlYXJjaF92NF8wIjoiUGJoX1NlYXJjaF9HZXQiLCJhbXIiOlsicGFzc3dvcmQiXX0.NpgG1Tf0c1Z_hm3VPmE1PM34xcCDiq--Ry665iq1J_xqZHoWz_D30i0Omr2tPFV-7BNJAuIBdV1M5rjXolPuz5V4pT25_fqmBnKDQ1bDbnEPu68nztRDaguPmWGLTkMAwkVuwPpwsBu18h9bOLAMB5h8W7tfMXXgeGXZSPOtUqqlTc_FFvJi9PN0B5OsI9J-wm_CpHEgmqkioHmHOPyWlAhyvHma6zh_cbMCNhtNOH0Fr4HJFsxEJexAr3mkGACXokSMbR6FElq9S6YF1enui8jRYt5c5nWmC_hqn6oxcoAvgtFncv_lQTHxok-bnjXeKpKa0DBoUCXUuI_QNE_mrQ'
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