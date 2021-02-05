#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
a = []
for i in soup.find_all('a'):
    if "#" in i.get('href'):
        pass
    else:
        a.append(i.get('href'))
a = list(set(a))
for i in range(len(a)):
    print a[i]
