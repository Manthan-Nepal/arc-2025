from http.server import HTTPServer, BaseHTTPRequestHandler

host= 'localhost'
port= 8000

class httpview(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello this is a http.server example.</h1></body></html>", "utf-8"))
        
server= HTTPServer((host, port), httpview)
print("Server running successful.")
try:
    server.serve_forever()
finally:
    server.server_close()
    print("Server stopped.")


