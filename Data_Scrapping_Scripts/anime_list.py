#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
f=open("anime2.lst","wt")
for i in range(1,50):
    url ="https://www20.gogoanimes.tv/anime-list.html?page=%d" %i
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    j = soup.find("div",{"class":"anime_list_body"})
    for i in j.find_all("a"):
        f.write((i.text + " : https://www20.gogoanimes.tv" + str(i.get("href"))).encode("utf-8")+"\n")
