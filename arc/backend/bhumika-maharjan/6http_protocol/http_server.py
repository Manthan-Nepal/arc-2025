# python -m http.server 8000


from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ('', 8000)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Serving on port 8000...")
httpd.serve_forever()
