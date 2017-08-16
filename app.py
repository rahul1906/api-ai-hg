#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


text = r"""
{"responseHeader":{"cid":"PBHTEST_007","cat":2,"q":"john","useexactmatch":false,"pt":null,"state":"CA","maxItems":5,"maxConditionItems":5,"maxDentistItems":5,"maxDentistPracticeItems":5,"maxLocationItems":5,"MaxFacilitiesPerGroup":5,"maxProviderPracticeItems":5,"maxProcedureItems":5,"maxProviderItems":5,"maxSpecialtyItems":5,"maxTopHospitalItems":5},"response":{"numCategories":1,"categories":[{"title":"Healthcare Providers Near {Location}","category":"Provider","catType":"Provider","suggestions":[{"content":{"hasContent":false},"entity":{"type":"Provider","profileUrl":"/physician/dr-biju-john-3yyj8","providerId":"3YYJ8","officeCode":"OOTH35B","providerNpi":"1073691705","providerFirstname":"Biju","providerLastname":"John"},"highlightedText":"<span class='name'>Dr. Biju <em>John</em>, MD</span>,&nbsp;<span class='location'>San Francisco, CA</span>","value":"Dr. Biju John, MD"},{"content":{"hasContent":false},"entity":{"type":"Provider","profileUrl":"/provider/alexander-john-33g54","providerId":"33G54","officeCode":"OO5DSN3","providerNpi":"1508881434","providerFirstname":"Alexander","providerLastname":"John"},"highlightedText":"<span class='name'>Alexander <em>John</em> Jr., CRNA</span>,&nbsp;<span class='location'>Clovis, CA</span>","value":"Alexander John Jr., CRNA"},{"content":{"hasContent":false},"entity":{"type":"Provider","profileUrl":"/dentist/dr-andrew-john-xhdns","providerId":"XHDNS","officeCode":"OO5DQXR","providerNpi":"1114163730","providerFirstname":"Andrew","providerLastname":"John"},"highlightedText":"<span class='name'>Dr. Andrew K. <em>John</em>, DDS</span>,&nbsp;<span class='location'>Oceanside, CA</span>","value":"Dr. Andrew K. John, DDS"},{"content":{"hasContent":false},"entity":{"type":"Provider","profileUrl":"/provider/kelly-john-yvjcr","providerId":"YVJCR","officeCode":"OO8JSCM","providerNpi":"1740451772","providerFirstname":"Kelly","providerLastname":"John"},"highlightedText":"<span class='name'>Kelly <em>John</em></span>,&nbsp;<span class='location'>Santa Cruz, CA</span>","value":"Kelly John"},{"content":{"hasContent":false},"entity":{"type":"Provider","profileUrl":"/provider/tiffany-john-3mfhr","providerId":"3MFHR","officeCode":"OO8MPDV","providerNpi":"1679882617","providerFirstname":"Tiffany","providerLastname":"John"},"highlightedText":"<span class='name'>Tiffany <em>John</em></span>,&nbsp;<span class='location'>Paradise, CA</span>","value":"Tiffany John"}]}]}}

"""

@app.route('/webhook', methods=['POST'])
def webhook():
    # req = request.get_json(silent=True, force=True)
    req = json.loads(text, strict=False)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    names = create_namelist(req)
    return create_messages(names)



def create_namelist(data):
    l = []
    for i in range(0, len(data['response']['categories'][0]['suggestions'])):
        l.append(data['response']['categories'][0]['suggestions'][i]['value'])
    return l


def create_messages(l):
    l1 = []
    for i in l:
        a = {"type":0,
        "speech":i}
        l1.append(a)
    return {"messages":l1}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')