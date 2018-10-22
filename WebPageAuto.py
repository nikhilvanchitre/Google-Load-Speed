# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:05:03 2018

@author: O37920
"""
import time
from urllib.request import urlopen

html = urlopen("https://www.webpagetest.org/runtest.php?f=json&url=https://www.coca-colaindia.com&k=A.f5ef07d94c752bb836266f6de35a8acc")
type(html)

data = html.read()

import json
d = json.loads(data)
link = d['data']['jsonUrl']
time.sleep(2)

report_html = urlopen(link)
report_data = report_html.read()
time.sleep(2)

report_json = json.loads(report_data)
report_onesite = report_json['data']['average']['firstView']
time.sleep(2)

type(report_onesite)

import pandas as pd
data_onesite = pd.DataFrame.from_dict(list(report_onesite.items()))
print(data_onesite)
