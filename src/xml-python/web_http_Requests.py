from httplib import HTTP
req = HTTP("www.example.com")
req.putrequest("GET", "/index.html")
req.putheader("Accept", "text/html")
req.putheader("User-Agent", "MyPythonScript")
req.endheaders()
ec, em, h = req.getreply()
print(ec, em)
# 200 OK
fd = req.getfile()
textlines = fd.read()
fd.close()