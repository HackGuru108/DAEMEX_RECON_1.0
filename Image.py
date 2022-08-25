import http.client

try:
    conn = http.client.HTTPConnection("www.google.com")
    conn.connect()    
except Exception as ex:
    print("Could not connect to page.")