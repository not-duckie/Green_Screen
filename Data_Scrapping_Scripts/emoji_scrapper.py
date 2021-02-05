#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import os
f = open(".emoji","wt")
url = "https://emojipedia.org/people/"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
j = soup.find('ul', { "class": "emoji-list" })
for i in j.find_all("a"):
     f.write("%s\n" %i.text.encode('utf-8'))
