import httplib
conn = httplib.HTTPConnection("quotes.prys.me.uk:3412")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print r1.status, r1.reason

