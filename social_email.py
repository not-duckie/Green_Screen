"""
The script is fine but the Emkeis Site now uses recaptcha so the script is marked as a robot and thus declined access.
"""



#!/usr/bin/env python

import mechanize

br = mechanize.Browser()
br.addheaders=[('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'),]
br.set_handle_robots(False)
br.open("https://127.0.0.1:8500/")
for i in  br.forms():
    print i

br.form['fromname']='Facebook'
br.form['form']='newsletter@runmailnetwork.in'
br.form['rcpt']='sarthakmisraa@gmail.com'
br.form['subject']='Fucked'
s=" well hello my name is locco and am a special pug, i live in belfert ireland and my favorite things are hug and wowowowowow"
br.form['text']=s
a = br.submit()
a.get_data
