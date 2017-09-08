<<<<<<< HEAD
import httplib
conn = httplib.HTTPConnection("quotes.prys.me.uk:3412")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
=======
import time
import urllib

var = 1
while var==1:
   try:
      print urllib.urlopen("http://quotes.prys.me.uk:3412/quote/random").getcode()
   except IOError:
      print "Error accessing website"
   time.sleep(5)
>>>>>>> 0325b73278beda41bba262e22713ef0f7186a7f3

