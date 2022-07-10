import sys
port='3000'

if sys.version_info < (3, 0):
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
else:
    from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(("127.0.0.1", int(port)), SimpleHTTPRequestHandler)
print("Serving HTTP on localhost port " + port + " (http://127.0.0.1:" + port + "/) ...")
httpd.serve_forever(3000)